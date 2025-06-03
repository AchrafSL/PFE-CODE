# DAMSO_STREAM - Web Application for Digital Services

## Overview

**DAMSO_STREAM** is an innovative web application designed to provide high-quality digital services at extremely competitive prices. Services include Netflix, Prime Video, Microsoft 365, Adobe Creative Cloud, and more. The application offers user-friendly navigation, secure payments, and a streamlined order process to make digital service acquisition accessible for everyone.

## Project Authors

- **Salimi Achraf**
- **Dongmo Kengmo Duclair**

## Supervisor

- **Pr. Enneya Nourddine**

---

## Features

### User Roles
- **Client**: View offers, manage subscriptions and orders, leave comments.
- **Employee**: Treat orders and communicate with clients.
- **Admin**: Full access including managing users, offers, orders, comments, and viewing statistics.

### Functionalities
- Account creation, login/logout, email verification, and password reset.
- Browsing and searching digital service offers.
- Dynamic shopping cart and order submission.
- Subscription tracking with automatic status updates.
- Admin and employee panels for system management.
- Comment sections for each offer.
- Email communication (SMTP via Gmail).
- Real-time data validation with **Axios**.

---

## Technologies Used

### Backend
- **Python 3**
- **Flask** (with Flask-Mail, MySQL Connector, Werkzeug)
- **MySQL**

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**
- **Jinja2 (template engine)**
- **Axios (for AJAX requests)**

### Additional Libraries
- **phonenumbers**: For international phone validation.
- **datetime**: For date and time management.

### Development Tools
- **Visual Studio Code**
- **Astah** (for UML modeling)

---

## Database Design

- **USER**: Stores user profiles and roles.
- **OFFERS**: Lists available digital service offers.
- **ORDERS & ORDEROFFERS**: Handle client orders.
- **CART & CARTOFFERS**: Temporary storage for selected services.
- **SUBSCRIPTION**: Tracks active/inactive subscriptions.
- **COMMENT**: Stores comments for each offer.

---

## UML Diagrams

- **Use Case Diagram**
- **Sequence Diagram**
- **Class Diagram**
- **Activity Diagram (Sign Up Flow)**

---

## Quality Assurance

- Client-side validation with **JavaScript + RegEx**
- Server-side validation using **Flask**
- Email verification before full account access
- Secure file upload handling
- Efficient error handling with Axios (without full page reloads)

---

## Deployment Notes

- Gmail SMTP used for email notifications (limit: ~2000 emails/day)
- Flask session management with 24h expiration
- Database relationships implemented with foreign keys and integrity constraints

---

## Known Limitations

- The platform is not responsive across all screen sizes (no media queries yet).
- Time constraints limited the addition of advanced UX/UI features.

---

## Future Improvements

- Responsive design using CSS Media Queries
- Admin dashboard with advanced analytics
- Mobile app version
- Improved file management and notification system

---

## Webography

- [Flask Docs - File Uploads](https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/)
- [UML Explanation](https://www.lucidchart.com/pages/fr/langage-uml)
- [HTML/CSS Basics](https://www.w3schools.com/)
- Full source list available in the original project document.

---

## License

This project is educational and non-commercial. All rights reserved to the authors.

