"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950) ).all()

# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    matches = Model.query.filter(Model.year == year).all()

    if matches:
        for match in matches:
            print "Model Name: ", match.name
            print "Brand Name: ", match.brand_name
            print "Brand HQ: ", match.brand.headquarters
    else:
        "No data found for that year."


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()

    brands_and_models = {}

    for brand in brands:
        brands_and_models[brand.name] = []
        for model in brand.models:
            brands_and_models[brand.name].append(model.name)
        print brand.name, ": ", brands_and_models[brand.name]


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# The returned value is: <flask_sqlalchemy.BaseQuery at 0x7f5bf807bd50>
# This is a list with one database object, representing the query we made,
# not the values associated with the query in the database. Having a base query
# object allows us to reuse the objects and access their properties. No results
# will be shown until we 'collect' data, with one(), first(), get(), or all(). 

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# An association table is a sort of bridge table. It is the connection between
# two tables that need to be connetced, but because "many to many" relationships
# are not technically possible, an association table is created.
# The main difference between an association table and a common table, is that an association
# table does not have any meaningful fields. It's sole purpose is to link two other
# tables together.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """returns a list of objects with the brands containing / are equal to the passed string"""

    return Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()


def get_models_between(start_year, end_year):
    """returns a list of objects with models between two years"""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
