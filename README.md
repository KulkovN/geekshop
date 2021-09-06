# GeekShop
Pet-project at Django-framework

How install:
1. from the folder for the project  (in your terminal) :
      
        git clone https://github.com/KulkovN/geekshop_ot_2.git
2. With pip in your terminal:

        pip install -r requirements.txt
3. Change django database settings to "default" (at SQLite, for demo and tests)
4. Create and migrate DB;
5. load data-dump:
      
        python3 manage.py loaddata datadump.json

From the backend functionality - implemented:

  - registration with activation by email / integration of login via VK (social network);
  - authorization;
  - editing a profile;
  - work with the catalog;

and other

Front functionality:

  - templates for bootstrap 5;
  - dynamic data change (Ajax-js) - not much at all. 


Screnshots:

    index:
![изображение](https://user-images.githubusercontent.com/68808458/132255743-b7d6b2d6-cd99-48e2-af18-c9d81503bac2.png)

    Contacts:

![изображение](https://user-images.githubusercontent.com/68808458/132255807-d8dfcaca-1e35-4b39-bf59-78b0670aee6e.png)

    Catalog:
![изображение](https://user-images.githubusercontent.com/68808458/132255881-ce8699a7-09b9-4b34-9ed1-9513d72d7812.png)

    Profile:
![изображение](https://user-images.githubusercontent.com/68808458/132255964-cbdb65ce-f141-4f2d-ac0d-afb567876a9c.png)

    Custom admin-panel:
![изображение](https://user-images.githubusercontent.com/68808458/132256012-919967d2-1cbb-46ec-a191-85dfc15dc22d.png)

    Orders starting:
![изображение](https://user-images.githubusercontent.com/68808458/132256149-cd597838-0320-409a-b501-8269f5340eca.png)

