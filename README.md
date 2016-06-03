# Python - Customer Search 

Let’s say we have some customer records in a text file (customers.txt, see below) – one customer per line, 
JSON-encoded. We want to invite any customer within 100km of our Dublin office (GPS coordinates 53.3381985, -6.2592576) 
for some food and drinks on us.

Write a program that will read the full list of customers and output the names and user ids of matching customers 
(within 100 km), sorted by user id (ascending).


## Basic Usage

### Import main library

```python
import core
from core.customers_wrapper import CustomersWrapper
```


### Utilize Facade CustomersWrapper to perform searches

```python
customers_wrapper = CustomersWrapper()
customers_nearby = customers_wrapper.get_customers_nearby(point, radius)
```

### Examples


#### Search customers within 100km of Intercom's Dublin office

``` python
import core
from core.customers_wrapper import CustomersWrapper
from core.spatial_point import SpatialPoint

dublin_office = SpatialPoint(53.3381985, -6.2592576, "Dublin Office")
radius = 100

customers_wrapper = CustomersWrapper()
customers_nearby = customers_wrapper.get_customers_nearby(dublin_office, radius)
```


## Running Tests

Unit tests:

```bash
nosetests tests/unit
```


## Architecture
- Facade pattern
- Template pattern

![architecture](https://raw.githubusercontent.com/jcast450/interview-prep/master/personal/intercom/architecture.png)
