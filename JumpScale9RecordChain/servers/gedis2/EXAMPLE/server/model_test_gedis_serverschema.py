

from js9 import j

JSBASE = j.application.jsbase_get_class()

SCHEMA="""
@url = test.gedis.serverschema
@name = schematest1
cmds = (LO) !test.gedis.cmd


"""

class schematest1(JSBASE):
    
    def __init__(self):
        JSBASE.__init__(self)        
        self.namespace = "schematest1"
        self.db = j.servers.gedis.latest.db
        self.table = self.db.tables["schematest1"]
        self.schema = self.table.schema

    def set(self,data,id=0):
        return self.table.set(data=data, id=id, hook=self.hook_set)

    def get(self,id,capnp=False):
        return self.table.get(id=id, capnp=capnp, hook=self.hook_get)

    def find(self,**args):
        return self.table.find(hook=self.hook_get,**args)
        
    def new(self):
        return self.table.new()

    def hook_set(self,obj):
        """
        before an object is set in the DB it will pass through this function, 
        this allows addional manipulation of object or security checks
        """
        return obj

    def hook_get(self,obj):
        """
        after an object is retreived from DB but before send to the consumer
        it will pass through this function, 
        this allows addional manipulation of object or security checks
        """
        return obj
