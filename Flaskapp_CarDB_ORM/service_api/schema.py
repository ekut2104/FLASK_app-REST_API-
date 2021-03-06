from Flaskapp_CarDB_ORM.service_api import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'age', 'email', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class NameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name')


name_schema = NameSchema()
names_schema = NameSchema(many=True)


class PersonSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'name_id')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
