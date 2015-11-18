<?php

namespace App\Http\Controllers;

use App\Services\CredlyApi;

class BaseController extends Controller {

    protected $CredlyApiClient;

    public function __construct() {
        $this->CredlyApiClient = new CredlyApi(
            new Client(['base_uri' => 'https://api.credly.com/1.1/'])
        );
    }
}

?>
