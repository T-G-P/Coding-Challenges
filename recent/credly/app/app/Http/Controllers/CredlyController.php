<?php

namespace App\Http\Controllers;

use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;

class CredlyController extends CredlyApiClientController{

    public function getBadges($id) {
        $res = [];
        try {
            $res = $this->CredlyApiClient->getBadges($id);
        } catch (RequestException $e) {
            $res = $e->getResponse()->getBody(true);
            return response()->json(json_decode($res));
        }
        return response()->json($res);
    }
}

?>
