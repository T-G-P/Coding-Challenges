<?php

namespace App\Api\V1\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use JWTAuth;
use App\User;
use Dingo\Api\Routing\Helpers;

use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\File;
Use Illuminate\Support\Facades\Validator;

class UserController extends Controller
{
    use Helpers;
    public function gallery()
    {
        //need to paginate data
		return User::with('comments', 'images')
            ->orderBy('created_at', 'DESC')
            ->simplePaginate(15);
    }
}
