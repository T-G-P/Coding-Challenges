<?php

namespace App\Api\V1\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use JWTAuth;
use App\Image;
use Dingo\Api\Routing\Helpers;

use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\File;
Use Illuminate\Support\Facades\Validator;

class ImageController extends Controller
{
    use Helpers;

    public function index()
    {
        $currentUser = JWTAuth::parseToken()->authenticate();
        return $currentUser
            ->images()
            ->orderBy('created_at', 'DESC')
            ->get()
            ->toArray();
    }

    public function show($id)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = $currentUser
            ->images()
            ->find($id);

        $path =  storage_path().'/uploads/' . $image->filename;

        if(!File::exists($path)) abort(404);

        $file = File::get($path);
        $type = File::mimeType($path);

        $response = Response::make($file, 200);
        $response->header("Content-Type", $type);

        return $response;

    }

    public function store(Request $request)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = new image;
        //$rules = array('image' => 'required');
        $rules = array();
        $file = array('image' => Input::file('image'));
        $validator = Validator::make($file, $rules);

        if(!empty($file['image']) && !$validator->fails()) {
            $originalFilename = Input::file('image')->getClientOriginalName();
            $extension = Input::file('image')->getClientOriginalExtension();
            $filename = time().'.'.$originalFilename;
            $image->metadata = $request->get('metadata');
            $image->user_id = $currentUser->id;
            $image->filename = $filename;
            if($currentUser->images()->save($image)) {
                $destinationPath = storage_path().'/uploads';
                Input::file('image')->move($destinationPath, $filename);
                return $this->response->created();
            }
        }
        return $this->response->error('could_not_create_image', 500);
    }

    //TODO

    // public function update($id)
    // {
    //     $currentUser = JWTAuth::parseToken()->authenticate();

    //     $image = $currentUser
    //         ->images()
    //         ->find($id);

    //     if(image) {
    //         $image->name = $request->get('name');
    //         $image->metadata = $request->get('metadata');
    //         $image->user_id = $currentUser->id;
    //         $currentUser->images()->save($image);
    //         return $this->response->updated();
    //     }
    //     else
    //         return $this->response->error('could_not_update_image', 500);
    // }

    // public function delete($id)
    // {
    //     $currentUser = JWTAuth::parseToken()->authenticate();

    //     $image = $currentUser
    //         ->images()
    //         ->find($id);

    //     if(image) {
    //         $currentUser->images()->delete($image);
    //         return $this->response->deleted();
    //     }
    //     else
    //         return $this->response->error('could_not_update_image', 500);
    // }
}
