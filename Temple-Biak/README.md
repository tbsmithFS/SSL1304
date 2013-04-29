Proj: Tempbiak
Copy: (c) 2013 Tempbiak

========

Lead Developer: Derek Temple
Developer/Designer: Biak Sang

========

Tempbiak is a microblogging site for sharing videos, photos, and articles from across the web.

========

Version 1 Features:
	- Registration/Login/Logout
	- Gravitar
	- Comment Style communication
	- Dashboard
		- User Control Panel
		- Contacts
	- Pages
		- Home
		- Contact Us
		- Posts (Template)
		- Dashboard (Template) (Protected)
	- Navigation
		- Home
		- Posts
		- Contact
	- Login form OR Username w/ link to dashboard

========
		
Version 2:
	- Gravitar
	- YouTube and Flickr API
	- Links with Social Networks
		- Share, Like, Tweet, +1

========

Database tables:
	- Users
		- userId
		- username
		- email -> Used for Gravitar
		- password
		- userType
		- last name

	- Post
		- postId
		- userID
		- postTitle
		- postContent
		- imageLink -> Flickr/PhotoBucket/etc API's
		- videoLink -> YouTube/Vimeo/etc API's
		- date

	- Comments
		- commentId
		- postId
		- userId
		- commentContent
		- date