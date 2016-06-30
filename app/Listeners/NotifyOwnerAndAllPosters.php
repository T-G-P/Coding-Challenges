<?php

namespace App\Listeners;

use App\Events\CommentWasPosted;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;
use Mail;

class NotifyOwnerAndAllPosters
{
    /**
     * Create the event listener.
     *
     * @return void
     */
    public function __construct()
    {
    }

    /**
     * Handle the event.
     * Send an email to the owner as well as all of the comment posters
     *
     * @param  CommentWasPosted  $event
     * @return void
     */
    public function handle(CommentWasPosted $event)
    {
        $image = $event->image;
        $owner = $image->user()->get();
        $comments = $image
            ->comments()
            ->orderBy('id', 'desc')
            ->get();

        $text = 'New activity on image'.$image->filename;
        foreach($comments as $comment) {
            $user = $comment->user()->first();
            Mail::raw($text, function ($m) use ($text, $user) {
                $m->from('hello@tobias.perelste.in', 'Adobe Test');
                $m->to($user->email, $user->name)->subject($text);
            });
        }
    }
}
