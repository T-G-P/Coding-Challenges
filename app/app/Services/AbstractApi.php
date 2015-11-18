<?php 

namespace App\Services;

use GuzzleHttp\Client;

class AbstractApi {

    protected $client;

    public function __construct(Client $client) {
        $this->client = $client;
    }
}
?>
