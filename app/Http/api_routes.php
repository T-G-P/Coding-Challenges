<?php

$api = app('Dingo\Api\Routing\Router');

$api->version('v1', function ($api) {

	$api->post('auth/login', 'App\Api\V1\Controllers\AuthController@login');
	$api->post('auth/signup', 'App\Api\V1\Controllers\AuthController@signup');
	$api->post('auth/recovery', 'App\Api\V1\Controllers\AuthController@recovery');
	$api->post('auth/reset', 'App\Api\V1\Controllers\AuthController@reset');


    $api->group(['middleware' => 'api.auth'], function ($api) {
        $api->get('images', 'App\Api\V1\Controllers\ImageController@index');
        $api->get('image/{id}', 'App\Api\V1\Controllers\ImageController@show');
        $api->post('images', 'App\Api\V1\Controllers\ImageController@store');
    });

    // guests can view users and their images
    // gallery endpoint to return all images with pagination
	$api->get('Users', function() {
		return \App\User::all();
	});
	$api->get('Images', function() {
		return \App\Image::all();
	});

});
