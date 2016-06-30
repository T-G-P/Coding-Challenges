# Adobe-Test
============

Currently supporting functionality for uploading images, retrieving images, adding comments, and viewing Users and Images.

TODO
Pagination for comments and images

Queuing all file system IO stuff for saving images

Sending email notifications to users when comments are posted

Rate limiting endpoints

Caching of requests

Unit tests


# API ROUTES
+-----------+---------------------------------------------------------+------+-------------------------------------------------+-----------+------------+----------+------------+
| Host      | URI                                                     | Name | Action                                          | Protected | Version(s) | Scope(s) | Rate Limit |
+-----------+---------------------------------------------------------+------+-------------------------------------------------+-----------+------------+----------+------------+
| localhost | POST /api/auth/login                                    |      | App\Api\V1\Controllers\AuthController@login     | No        | v1         |          |            |
| localhost | POST /api/auth/signup                                   |      | App\Api\V1\Controllers\AuthController@signup    | No        | v1         |          |            |
| localhost | POST /api/auth/recovery                                 |      | App\Api\V1\Controllers\AuthController@recovery  | No        | v1         |          |            |
| localhost | POST /api/auth/reset                                    |      | App\Api\V1\Controllers\AuthController@reset     | No        | v1         |          |            |
| localhost | GET|HEAD /api/users/images                              |      | App\Api\V1\Controllers\ImageController@index    | Yes       | v1         |          |            |
| localhost | POST /api/users/images                                  |      | App\Api\V1\Controllers\ImageController@store    | Yes       | v1         |          |            |
| localhost | GET|HEAD /api/users/image/{id}                          |      | App\Api\V1\Controllers\ImageController@show     | Yes       | v1         |          |            |
| localhost | PUT /api/users/image/{id}                               |      | App\Api\V1\Controllers\ImageController@update   | Yes       | v1         |          |            |
| localhost | DELETE /api/users/image/{id}                            |      | App\Api\V1\Controllers\ImageController@delete   | Yes       | v1         |          |            |
| localhost | GET|HEAD /api/users/comments                            |      | App\Api\V1\Controllers\CommentController@index  | Yes       | v1         |          |            |
| localhost | GET|HEAD /api/users/image/{imageId}/comment/{commentId} |      | App\Api\V1\Controllers\CommentController@show   | Yes       | v1         |          |            |
| localhost | POST /api/users/image/{imageId}/comments                |      | App\Api\V1\Controllers\CommentController@store  | Yes       | v1         |          |            |
| localhost | DELETE /api/users/image/{imageId}/comment/{commentId}   |      | App\Api\V1\Controllers\CommentController@delete | Yes       | v1         |          |            |
| localhost | GET|HEAD /api/images                                    |      | App\Api\V1\Controllers\ImageController@gallery  | No        | v1         |          |            |
| localhost | GET|HEAD /api/users                                     |      | App\Api\V1\Controllers\UserController@gallery   | No        | v1         |          |            |
+-----------+---------------------------------------------------------+------+-------------------------------------------------+-----------+------------+----------+------------+
