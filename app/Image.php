<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Image extends Model
{
    protected $fillable = ['filename', 'user_id', 'metadata'];

    public function comments()
    {
        return $this->hasMany('App\Comment');
    }
}
