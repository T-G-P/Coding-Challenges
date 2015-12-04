<?php 

namespace App\Services;


class CredlyApi extends AbstractApi {

    public function getBadges($id) {
        $response = $this->client->request(
            'GET',
            'badges/',
            [
                'query' => [
                    'verbose' => 1,
                    'access_token' => env('CREDLY_TOKEN')
                ],
                'headers' => [
                    'X-Api-Key' => env('CREDLY_API_KEY'),
                    'X-Api-Secret' => env('CREDLY_API_SECRET')
                ],
            ]
        );

        return json_decode($response->getBody());
    }
}

?>
