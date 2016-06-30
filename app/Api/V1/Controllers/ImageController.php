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

    public function gallery()
    {
		return Image::simplePaginate(15);
    }

    public function index()
    {
        $currentUser = JWTAuth::parseToken()->authenticate();
        return $currentUser
            ->images()
            ->with('comments')
            ->orderBy('created_at', 'DESC')
            ->simplePaginate(15);
    }

    public function show($id)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = $currentUser
            ->images()
            ->with('comments')
            ->find($id);

        if(!$image) abort(404);

        $path = $image->serverpath;

        if(!File::exists($path)) abort(404);

        return $this->response()->array($image)->statusCode(200);
    }

    public function store(Request $request)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = new image;

        $res = $this->_validateAndSaveFile($currentUser, $image, $request);

        if(!empty($res['error'])) {
            return $this->response->error($res['error'], $res['statuscode']);
        }
        return $this->response()->array($res['image'])->statusCode($res['statuscode']);
    }

    public function update(Request $request, $id)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = $currentUser
            ->images()
            ->with('comments')
            ->find($id);

        if(!$image) abort(404);

        $res = $this->_validateAndSaveFile($currentUser, $image, $request);

        if(!empty($res['error'])) {
            return $this->response->error($res['error'], $res['statuscode']);
        }
        return $this->response()->array($res['image'])->statusCode($res['statuscode']);

    }

    public function delete(Request $request, $id)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = $currentUser
            ->images()
            ->with('comments')
            ->find($id);

        if(!$image) abort(404);

        $res = $this->_validateAndSaveFile($currentUser, $image, $request);

        if(!empty($res['error'])) {
            return $this->response->error($res['error'], $res['statuscode']);
        }
        if($image->delete()) {
            return $this->response()->array($res['image'])->statusCode($res['statuscode']);
        }
        return $this->response->error('Unable to delete file', 500);
    }

    /*Will need to extract file io stuff from here and queue the saving aspects*/
    private function _validateAndSaveFile($currentUser, $image, $request)
    {
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
            $image->serverpath =  storage_path().'/uploads/' . $image->filename;

            if($currentUser->images()->save($image)) {
                $destinationPath = storage_path().'/uploads';
                $statuscode = 200;

                if ($request->isMethod('post'))
                    $statuscode = 201;

                Input::file('image')->move($destinationPath, $filename);

                return array('image' => $image, 'statuscode' => $statuscode);
            }
        }
        return array('error' => "Unable to process file", 'statuscode' => 500);
    }
}
