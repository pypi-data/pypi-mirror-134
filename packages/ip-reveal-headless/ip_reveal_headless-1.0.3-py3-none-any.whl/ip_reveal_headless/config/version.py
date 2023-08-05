from johnnydep.lib import JohnnyDist


class Version(object):
    
    class Update(object):
        def __init__(self, avail_version):
            self.available_version = avail_version
        
    
    def __init__(self):
        self.prog_name = 'IP-Reveal-Headless'
        self.dist = JohnnyDist(self.prog_name)
        self.current = self.dist.version_installed
        self.bleeding_latest = self.dist.version_latest
        self.stable_latest = self.dist.version_latest_in_spec
        self.version_list = self.dist.versions_available
        self.outdated = self.needs_update
        
        if self.latest == self.current:
            self.Update = None
        else:
            self.Update = self.Update(avail_version=self.current)
        
    @property
    def latest(self):
        return self.dist.version_latest
        
    @property
    def needs_update(self):
        if self.Update:
            return True
        else:
            return False
        
    
    def __repr__(self, full=False):
        returning = ''
        if full:
            returning += self.prog_name + f' | {self.current}'
            if self.needs_update:
                returning += f' | Update Available ({self.Update.available_version})'
            
        else:
            return self.current
    
    
VERSION = Version()
    
