<?php

namespace App\Http\Controllers;

use App\Services\CredlyApi;
use GuzzleHttp\Client;

class CredlyApiClientController extends Controller {

    protected $CredlyApiClient;

    public function __construct() {
        $this->CredlyApiClient = new CredlyApi(
            new Client(['base_uri' => 'https://api.credly.com/v1.1/'])
        );
    }
}

?>
