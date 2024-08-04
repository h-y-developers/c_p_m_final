from import_export import resources
from ..models import User,Marks
class studentResource(resources.ModelResource):
    class Meta:
        model = User

class studentmarksResource(resources.ModelResource):
    class Meta:
        model = Marks