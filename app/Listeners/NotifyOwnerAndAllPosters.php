<?php

namespace App\Listeners;

use App\Events\CommentWasPosted;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;

class NotifyOwnerAndAllPosters
{
    /**
     * Create the event listener.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }

    /**
     * Handle the event.
     *
     * @param  CommentWasPosted  $event
     * @return void
     */
    public function handle(CommentWasPosted $event)
    {
        //
    }
}
