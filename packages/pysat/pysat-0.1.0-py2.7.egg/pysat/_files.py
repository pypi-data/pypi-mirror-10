import string
import os
import weakref
import re
import glob
import numpy as np
import pandas as pds


from pysat import data_dir as data_dir


class Files(object):
    
    def __init__(self, sat):
        self._sat = weakref.proxy(sat)
        self.base_path = os.path.join(os.getenv('HOME'), '.pysat')
        self.start_date = None
        self.stop_date = None
        self.files = pds.Series(None)
        self.data_path = os.path.join(data_dir,self._sat.platform, self._sat.name, self._sat.tag)
        
        if self._sat.platform != '':
            info = self._load()#self._sat.platform, self._sat.name, self._sat.tag)
       	    if info is not False:
       	        self._attach_files(info)
       	    else:
       	        print "pysat is searching for the requested instrument's files."
   	        # couldn't find stored info, load file list and then store
   	        info = self._sat._list_rtn(tag=self._sat.tag, data_path=self.data_path)
                if info is not None:
                    if len(info) > 0:
                        info = self._remove_data_dir_path(info)	
       	                self._attach_files(info)
       	                self._store()

    def _attach_files(self, files_info):
        """Attaches info returned by instrument list_files routine to Instrument object."""

	if (len(files_info.unique()) != len(files_info)): 
	    raise ValueError('List of files must have unique datetimes.')
   
	self.files = files_info.sort_index()
	date = files_info.index[0] 
	self.start_date = pds.datetime(date.year, date.month, date.day)
	date = files_info.index[-1] 
	self.stop_date = pds.datetime(date.year, date.month, date.day)

                
    def _store(self, dir=None):
        """Store currently loaded filelist for instrument onto filesystem"""
        name = ''.join((self._sat.platform,'_',self._sat.name,'_',self._sat.tag,
                        '_stored_file_info.txt'))
        if dir is None:
            name = os.path.join(self.base_path, name)
        else:
            name = os.path.join(dir, name)
        try:
            self.files.to_csv(name)
            return True
        except IOError:
            return False	


    def _load(self):
        """Load stored filelist and return as Pandas Series"""
        fname = ''.join((self._sat.platform,'_',self._sat.name,'_',
                        self._sat.tag, '_stored_file_info.txt'))
        fname = os.path.join(self.base_path, fname)
        try:
            data = pds.Series.from_csv(fname, index_col=0)
        except IOError:
            return False
        else:
            return data


    def refresh(self, store=False):
        """Refresh loaded instrument filelist by searching filesystem."""
        info = self._sat._list_rtn(tag=self._sat.tag, data_path=self.data_path)
        info = self._remove_data_dir_path(info)
        self._attach_files(info)
        if store:
            self._store()
        
    
    def get_new(self):
        """List all files on filesystem that weren't there the last time
           the file list was stored.
        """
        storedInfo = self._load()
        if storedInfo is not False:
            newInfo = self._sat._list_rtn(tag = self._sat.tag, data_path=self.data_path)
            newInfo = self._remove_data_dir_path(newInfo)
            boolArr = newInfo.isin(storedInfo) 
            newFiles = newInfo[~boolArr]
            return newFiles
        else:
            print 'No previously stored files that we may compare to.'
            return False

    def get_index(self, fname):
        """Return index in objects file_list for a particular filename. """
        idx, = np.where(fname == self.files)
        if len(idx) == 0:
            #filename not in index, try reloading files from disk
            self.refresh()
            idx, = np.where(fname == self.files)
            if len(idx) == 0:
		raise IOError('Could not find supplied file on disk')
	return idx 
	
    #convert this to a normal get so files[in:in2] gives the same as requested here
    #support slicing via date, filename, and index
    #filename is inclusive slicing, date and index are normal non-inclusive end point
    #is this hidden behavior good though?????	
    # I havent actually implemented difference in slicing yet   	  	
    def __getitem__(self, key):
        if isinstance(key, slice):
            try:
                out = self.files.ix[key]
	    except IndexError:
	        raise IndexError('Date requested outside file bounds.')                
            if len(out) > 1:
                if out.index[-1] >= key.stop:
                    return out[:-1]
                else:
                    return out
            elif len(out) == 1:
                if out.index[0] >= key.stop:
                    return pds.Series([])
                else:
                    return out
            else:
                return out
        else:
            raise ValueError('Not implemented yet.')         
        #if isinstance(key, tuple):
        #    if len(key) == 2:
        #        start = key[0]
        #        end = key[1]
        #    else:
        #        raise ValueError('Must input 2 and only 2 items/iterables')
                
    def get_file_array(self, start, end):
        """Return a list of filenames between and including start and end.
        
        paramters:
            start: list or single string of filenames for start of list
            stop: list or single string of filenames inclusive end of list
        returns:
            list of filenames between and including start and end over all
            intervals. 
            """
        if hasattr(start, '__iter__') & hasattr(end, '__iter__'):
            files = []
            for (sta,stp) in zip(start, end):
                id1 = self.get_index(sta)
		id2 = self.get_index(stp)
		files.extend(self.files[id1 : id2+1])
	elif hasattr(start, '__iter__') | hasattr(end, '__iter__'):
	    raise ValueError('Either both or none of the inputs need to be iterable')
        else:
            id1 = self.get_index(start)
	    id2 = self.get_index(end)
	    files = self.files[id1:id2+1].to_list()   
	return files
	                      
    def _remove_data_dir_path(self, inp=None):
        """Remove the data directory path from filenames"""
        # need to add a check in here to make sure data_dir path is actually in
        # the filename
        if inp is not None:
            match = os.path.join(self.data_path,'')
            num = len(match)	 
            return inp.apply(lambda x: x[num:])	
        
    @classmethod    
    def from_os(cls, data_path=None, format_str=None, 
                two_digit_year_break=None):
        """
        Produces a list of files and and formats it for Files class.
        """
        from utils import create_datetime_index
        if (format_str is None):
            raise ValueError("Must supply a filename template (format_str).")
        if (data_path is None):
            raise ValueError("Must supply instrument directory path (dir_path)")
        
        # parse format string to figure out the search string to use
        # to identify files in the filesystem
        search_str = ''
        form = string.Formatter()
        keys = []
        snips = []
        length = []
        stored = {'year':[], 'month':[], 'day':[], 'hour':[], 'min':[], 'sec':[]}
        for snip in form.parse(format_str):
            search_str += snip[0]
            snips.append(snip[0])
            if snip[1] is not None:
                keys.append(snip[1])
                search_str += '*'
                # try and determine formatting width
                temp = re.findall(r'\d+', snip[2])
                if temp:
                    # there are items, try and grab width
                    for i in temp:
                        if i != 0:
                            length.append(int(i))
                            break
                else:
                    raise ValueError("Couldn't determine formatting width")

        abs_search_str = os.path.join(data_path, search_str)
        files = glob.glob(abs_search_str)   
        
        # we have a list of files, now we need to extract the date information        
        # code below works, but only if the size of file string 
        # remains unchanged
        
        # determine the loactaions the date information in a filename is stored
        # use these indices to slice out date from loaded filenames
        #test_str = format_str.format(**periods)  
        if len(files) > 0:  
            idx = 0
            begin_key = []
            end_key = []
            for i,snip in enumerate(snips):
                #if snip is not None:
                #begin_lit.append(test_str.find(snip,idx) )
                #end_lit.append(begin_lit[-1] + len(snip))
                #idx = end_lit[-1]
                idx += len(snip)
                if i < (len(length)):
                    begin_key.append(idx)
                    idx += length[i]
                    end_key.append(idx)
            max_len = idx
            # setting up negative indexing to pick out filenames
            key_str_idx = [np.array(begin_key, dtype=int) - max_len, 
                            np.array(end_key, dtype=int) - max_len]
            #print key_str_idx
            # need to parse out dates for datetime index
            for i,temp in enumerate(files):
                for j,key in enumerate(keys):
                    val = temp[key_str_idx[0][j]:key_str_idx[1][j]]
                    stored[key].append(val)
    
            # convert to numpy arrays
            for key in stored.keys():
                stored[key] = np.array(stored[key]).astype(int)
                if len(stored[key]) == 0:
                    stored[key]=None
            
            # deal with the possibility of two digit years
            # years above or equal to break are considered to be 1900+
            # years below break are considered to be 2000+
            if two_digit_year_break is not None:
                idx, = np.where(stored['year'] >= two_digit_year_break)
                stored['year'][idx] = stored['year'][idx] + 1900
                idx, = np.where(stored['year'] < two_digit_year_break)
                stored['year'][idx] = stored['year'][idx] + 2000            
    
            index = create_datetime_index(year=stored['year'], month=stored['month'], 
                                    doy=stored['day'], uts=stored['sec'])

            return pds.Series(files, index=index)
        else:
            print ("Unable to find any files. If you have the necessary files "+
                    "please check pysat settings and file locations.") 

        