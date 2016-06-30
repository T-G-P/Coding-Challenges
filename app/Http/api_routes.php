<?php

$api = app('Dingo\Api\Routing\Router');

$api->version('v1', function ($api) {

	$api->post('auth/login', 'App\Api\V1\Controllers\AuthController@login');
	$api->post('auth/signup', 'App\Api\V1\Controllers\AuthController@signup');
	$api->post('auth/recovery', 'App\Api\V1\Controllers\AuthController@recovery');
	$api->post('auth/reset', 'App\Api\V1\Controllers\AuthController@reset');


    $api->group(['middleware' => 'api.auth'], function ($api) {
        //image related endpoints
        $api->get('users/images', 'App\Api\V1\Controllers\ImageController@index');
        $api->post('users/images', 'App\Api\V1\Controllers\ImageController@store');
        $api->get('users/image/{id}', 'App\Api\V1\Controllers\ImageController@show');
        $api->put('users/image/{id}', 'App\Api\V1\Controllers\ImageController@update');
        $api->delete('users/image/{id}', 'App\Api\V1\Controllers\ImageController@delete');

        // comments related endpoints
        $api->get('users/comments', 'App\Api\V1\Controllers\CommentController@index');
        $api->get('users/image/{imageId}/comment/{commentId}', 'App\Api\V1\Controllers\CommentController@show');
        $api->post('users/image/{imageId}/comments', 'App\Api\V1\Controllers\CommentController@store');
        $api->delete('users/image/{imageId}/comment/{commentId}', 'App\Api\V1\Controllers\CommentController@delete');
    });

    // guests can view users and their images
    // gallery endpoint to return all images with pagination
    // need to paginate
    $api->get('images', 'App\Api\V1\Controllers\ImageController@gallery');
    $api->get('users', 'App\Api\V1\Controllers\UserController@gallery');


});
