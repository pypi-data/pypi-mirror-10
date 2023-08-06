Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Description: [![Build Status](https://travis-ci.org/touilleMan/marshmallow-mongoengine.svg?branch=master)](https://travis-ci.org/touilleMan/marshmallow-mongoengine)
        
        # Marshmallow-Mongoengine
        
        ## Introduction
        
        Mongoengine integration with the marshmallow (de)serialization library.
        
        Heavilly ~~ripped~~ inspired by [marshmallow-sqlalchemy](http://marshmallow-sqlalchemy.rtfd.org/)
        
        ## Declare your models
        
        ```
        import mongoengine as me
        
        class Author(me.Document):
            id = me.IntField(primary_key=True, default=1)
            name = me.StringField()
            books = me.ListField(me.ReferenceField('Book'))
        
            def __repr__(self):
                return '<Author(name={self.name!r})>'.format(self=self)
        
        
        class Book(me.Document):
            title = me.StringField()
        ```
        
        ## Generate marshmallow schemas
        
        ```
        from marshmallow_mongoengine import ModelSchema
        
        class AuthorSchema(ModelSchema):
            class Meta:
                model = Author
        
        class BookSchema(ModelSchema):
            class Meta:
                model = Book
        
        author_schema = AuthorSchema()
        ```
        
        ## (De)serialize your data
        
        ```
        author = Author(name='Chuck Paluhniuk').save()
        book = Book(title='Fight Club', author=author).save()
        
        dump_data = author_schema.dump(author).data
        # {'id': 1, 'name': 'Chuck Paluhniuk', 'books': ['5578726b7a58012298a5a7e2']}
        
        author_schema.load(dump_data).data
        # <Author(name='Chuck Paluhniuk')>
        ```
        
Keywords: mongoengine marshmallow
Platform: UNKNOWN
Classifier: Intended Audience :: Developers
Classifier: License :: OSI Approved :: MIT License
Classifier: Natural Language :: English
Classifier: Programming Language :: Python :: 2
Classifier: Programming Language :: Python :: 2.7
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.3
Classifier: Programming Language :: Python :: 3.4
