# Enterprise Resource Planning MP
Django based Web Application to store & retrieve critical information about the SKUs of medicines across all pharmacies for a company along with the customer & supplier information in a database.

This application deprecates the need to manually log the SKUs of each medicine across the shops in for a chain of pharmacies and it can directly place an order to their suppliers if a particular medicine was close to running out of stock.

## Installation
- Install [Django](https://docs.djangoproject.com/en/3.1/intro/install/) if you haven't already.
- Add all the required packages for this application by applying the command mentioned below. 
```bash
pip install requirements.txt
```
- Install the application by applying the commands mentioned below.
 ```python
  python manage.py makemigrations
  python manage.py migrate
```
- Run the application server by applying the command `python manage.py runserver`

```BD```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
