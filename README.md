# django-rest-api-demo-service

This service is responsible to illustrate django rest inside docker container
Added pre commit configuration

# Reference

https://docs.docker.com/compose/django/

# Prerequisites

python3 and docker

docker --version
python3 --version
python3 -m django --version or pip show django
python3 -m djangorestframework --version

# migrations and create app

to run any migrations or create app you will have to go inside docker container
docker exec -it <container_id> bash

# Django Concepts

functional views - if you want to write your own custom logic

class based views - provides a wrapper so that you write less code
Here you have mixins, generics and viewsets

python manage.py shell - this will create a special terminal where you can import your models
and query them to see database results
eg. from blog.modesl import Post
Post.objects.all() - get all posts from db

- test django apps you can use package pytest-django
- to see code coverage results we can use package pytest-cov

APIView - provides each of the http methods, used when you want to define any method explicitly
primary key based operations -
non-primary key based operations - get, post

you can define one to many relationships with foreign keys. This is also
called nested searialization.
eg. One author can have many books. On delete of author all his books should be deleted. This is
setup using cascade

<!-- class Author(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)

    def __str__(self):
        return self.firstName

class Book(models.Model):
    title=models.CharField(max_length=50)
    ratings=models.CharField(max_length=10)
    author=models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) -->

# Python Concepts

help(str.concat) = will give definition of built in functions
dir(str) = gives lists of available methods
type(<variable>) = gives type of that variable like str, int, etc...
pep8 - lists down standard coding styles in python
you can create virtual env using venv module of python
bool() and 'is' keyword is used to find truthy or falsy values
bool is like ==
is compares to ===
logical operators = and, not, or
to remove duplicates from list you can use set and then loop over it and store contents in another list
since sets do not have order
numbers_list = [1, 23 , 23,]
set(numbers_list) -> returns {1, 23}
request is a package similar to fetch in javascript
try except is similar to try catch

# Pytest

pip install pytest in your virtual env
to run any test just run 'pytest' or pytest with -v flag for more detailed output
if you functiona name starts with 'test\_' then pytest will run it, thats how it recognises
tests to run

you can create pytest.ini file for any configurations related to pytest
functions are used as test cases and classes are used as test suites
eg.

<!-- [pytest]
python_files = test_*
python_classes = *Tests
python_functions = test_* -->

eg test stub

<!-- def test_checking:
  assert True -->

A good practice is to name the test file include its parent folder name,
that way you can create different folders for say regression, smoke, unit, e2e and then
any of them individually using markers(lets you create suites)

eg, run only tests with marker engine
@mark.engine
def ...

in the terminal run pytest -m engine

you could have multiple markers, lets say you have two components and you want
both of them to be covered in smoke test.

@mark.smoke
@mark.engine
def ...

run tests with multiple markers
pytest -m "body or engine"
pytest -m "not entertainment" - run all tests except entertainment

However, the best way to create suite is using class and then mark that class
this way all the methods will get that marker and you don't have to mark
each one individually

@mark.smoke

<!-- class SmokeTests:
  def demo (self):
    assert True -->

...

remember your markers by entering them in the pytest.ini file
markers =
smoke: ...
body: ...
regression: ...

get list of pytest default markers -> pytest --markers

- you can use fixtures for code that is used in multiple files.
- fixtures have scope like function, session
- wherever you add fixtures file you can use it in any directory which is
  sibling or child of it.

to generate reports you can use pytest-html
and then run in terminal pytest --html=results.html

pytest <path of files to run> -v

skip test
@pytest.mark.skip
@pytest.mark.skipif(4 > 1, reason="Skipped for testing")

if your test case fails pytest will stop execution. You can use xfail marker to continue execution
even if particular test case fails
@pytest.mark.xfail

when you want to run same test but with different args you can use parametrize marker
@pytest.mark.parametrize("a,b", [
{2, 3},
{4, 5}
])
def ...
