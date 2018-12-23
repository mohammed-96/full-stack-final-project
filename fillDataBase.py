from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from database import Category
from database import CategoryItem

engine = create_engine('sqlite:///categoryItems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Items for Apple

company1 = Category(name="Apple")

session.add(company1)
session.commit()

CategoryItem1 = CategoryItem(name="iPhone XR",
                             description="""All-screen design. Longest battery
                             life ever in an iPhone. Fastest performance.
                             And studio-quality photos. Trade in your
                             current iPhone and upgrade to iPhone XR.""",
                             price="$449",  category=company1)

session.add(CategoryItem1)
session.commit()


# Items for Samsung
company2 = Category(name="Samsung")

session.add(company2)
session.commit()


CategoryItem1 = CategoryItem(name="Galaxy S9+",
                             description="""Explore the innovations on Galaxy
                             S9 and S9+ that change
                             how you experience the world.""",
                             price="$739.99", category=company2)
session.add(CategoryItem1)
session.commit()

# Items for Huawei
company3 = Category(name="Huawei")
session.add(company3)
session.commit()

CategoryItem1 = CategoryItem(name="Mate 20 Pro",
                             description="""Limitless human imagination that’s
                             the inspiration for the HUAWEI Mate 20 Pro.""",
                             price="$800",  category=company3)
session.add(CategoryItem1)
session.commit()


print("added items!")
