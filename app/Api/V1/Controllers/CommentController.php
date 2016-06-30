<?php

namespace App\Api\V1\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Response;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use JWTAuth;
use App\Comment;
use Dingo\Api\Routing\Helpers;

use Illuminate\Support\Facades\Input;
use Illuminate\Support\Facades\File;
Use Illuminate\Support\Facades\Validator;

class CommentController extends Controller
{
    use Helpers;

    public function index()
    {
        $currentUser = JWTAuth::parseToken()->authenticate();
        return $currentUser
            ->comments()
            ->orderBy('created_at', 'DESC')
            ->get()
            ->toArray();
    }

    public function show($imageId, $commentId)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $image = $currentUser
            ->images()
            ->find($imageId);
        if(!$image) abort(404);

        $comment = $image
            ->comments()
            ->find($commentId);
        if(!$comment) abort(404);

        return $this->response()->array($comment)->statusCode(200);
    }

    public function store(Request $request, $imageId)
    {
        $currentUser = JWTAuth::parseToken()->authenticate();

        $reqComment = $request->get('comment');
        if(!$reqComment)
            return $this->response()->error('Cannot post empty comment', 500);

        $comment = new comment;
        $comment->comment = $reqComment;
        $comment->user_id = $currentUser->id;
        $comment->image_id = $imageId;

        if($currentUser->comments()->save($comment) && $currentUser->images()->save($comment))
            return $this->response()->array($comment)->statusCode(201);

        return $this->response->error('Unable to post comment', 500);
    }
}
