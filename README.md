![Backend](backend.jpeg)

# Django E-commerce Backend API

A simple yet robust e-commerce backend built with Django REST Framework, featuring user authentication, product catalog, shopping cart, wishlist, and order management with payment simulation.  
This project uses JWT authentication and supports admin analytics.

---

## Features

- Custom user model with email-based authentication  
- Product categories and detailed product info  
- Shopping cart with add/remove items  
- Wishlist management  
- Order placement and payment simulation  
- Admin-only sales analytics endpoint  
- JWT-based token authentication and registration endpoints

---

## Tech Stack

- Python 3.x  
- Django 5.2  
- Django REST Framework  
- Simple JWT for authentication  
- SQLite (default DB, easy to switch)

---

## Getting Started

### Prerequisites

- Python 3.8+  
- pip (Python package manager)  
- Git (optional, for cloning repo)

### Installation

1. Clone the repository  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### Database Setup

This project uses SQLite by default. To set up the database, run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

These commands will create the necessary tables based on the defined models.

---

### Running the Server

Start the development server with:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

---

## API Endpoints

### Authentication

* **Register new user**
  `POST /register/`
  Request body:

  ```json
  {
    "email": "user@example.com",
    "password": "yourpassword",
    "password2": "yourpassword",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```

  Response:

  ```json
  { "message": "User registered successfully." }
  ```

* **Login (JWT Token obtain)**
  `POST /api/token/`
  Request body:

  ```json
  {
    "email": "user@example.com",
    "password": "yourpassword"
  }
  ```

  Response:

  ```json
  {
    "refresh": "<token>",
    "access": "<token>"
  }
  ```

* **Refresh token**
  `POST /api/token/refresh/`
  Request body:

  ```json
  {
    "refresh": "<refresh_token>"
  }
  ```

  Response:

  ```json
  {
    "access": "<new_access_token>"
  }
  ```

---

### Products & Categories

* **List products (with pagination, search, filter)**
  `GET /api/products/`
  Query parameters:

  * `page` (optional)
  * `page_size` (optional)
  * `search` (search title/description)
  * `ordering` (`price` or `title`)
  * `category` (slug filter)

* **Retrieve a product**
  `GET /api/products/{id}/`

* **List categories**
  `GET /api/categories/`

* **Retrieve a category**
  `GET /api/categories/{id}/`

---

### Cart

* **Get current user's cart**
  `GET /cart/`
  Response includes cart items with product details and quantity.

* **Add an item to the cart**
  `POST /cart/`
  Request body:

  ```json
  {
    "product_id": 1,
    "quantity": 2
  }
  ```

  Response includes the newly added cart item.

* **Remove item from cart**
  `DELETE /cart/item/{cart_item_id}/`

---

### Wishlist

* **Get current user's wishlist**
  `GET /wishlist/`

* **Add/remove products to/from wishlist**
  `POST /wishlist/`
  Request body example to replace wishlist products:

  ```json
  {
    "product_ids": [1, 2, 3]
  }
  ```

  Partial updates supported; you can add/remove items by sending updated lists.

---

### Orders

* **List user orders**
  `GET /orders/`
  Returns a list of orders with details including items and payment status.

* **Place a new order (from current cart)**
  `POST /orders/`
  Creates an order from all items in the cart, then clears the cart.

* **Pay for an order**
  `POST /orders/{order_id}/pay/`
  Simulates payment by marking order as paid and timestamping.

---

### Admin Analytics (Admin Only)

* **Sales summary**
  `GET /admin/analytics/`
  Returns total revenue, total orders, paid orders, and top 5 best-selling products.

---

## Additional Notes

* Make sure to include the JWT `Authorization: Bearer <access_token>` header for authenticated endpoints.
* For media (product images), ensure media serving is configured properly in production (not covered here).
* Extend the User model or permissions as needed for admin or staff roles.
* Run `python manage.py createsuperuser` to create an admin user.
* For deployment, update `ALLOWED_HOSTS` and disable debug.

---

## Contributing

Feel free to open issues or submit pull requests to improve this project.

---

## License

This project is licensed under the MIT License.

---

## Contact

Created by \[MuhidTech] — \[[muhidtech77@gmail.com](mailto:muhidtech77@gmail.com)]
GitHub: \[[https://github.com/muhidtech](https://github.com/muhidtech)]