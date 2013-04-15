<?php

/*
    This is our main interface for the user
    for handling the displaying of static pages
*/

require_once 'models/view.php';

class Utilities {
    function get($pairs, $data = '') {

        if (empty($pairs['action'])) {
            $action = 'bathrooms';
        } else {
            $action = $pairs['action'];
        }

        $view_model = new View();
        $view_model->getView("header");

        if ($action == 'bathrooms') {
            $data = array(
                'type' => 'bathrooms',
                'listings' => array(
                array( 'name' => 'school bldg 3',
                  'rating' => 4,
                  'location' => "lat long",
                  'comments' => "can only get in if you're student or faculty",
                  ),
                array( 'name' => 'publix',
                  'rating' => 3,
                  'location' => "lat2 long2", 
                  'comments' => "don't have to buy anything",
                  ),
                array( 'name' => "Tony's pizza",
                  'rating' => 2,
                  'location' => "lat3 long3", 
                  'comments' => "have to buy something",
                  )
                  )
                  );
            $view_model->getView('utilities_list', $data);
        } else if ($action = 'electricity') {
            $data = array(
                'type' => 'electricity',
                'listings' => array(
                array( 'name' => 'Crispers',
                  'rating' => 4,
                  'location' => "lat long" ,
                  'comments' => "sit in the booths on the left",
                  ),
                array( 'name' => 'Starbucks',
                  'rating' => 3,
                  'location' => "lat2 long2",
                  'comments' => "plugs are under the tables near the counter"
                  ),
                array( 'name' => 'Walgreens',
                  'rating' => 1,
                  'location' => "lat4 long4",
                  'comments' => "in the back"
                  ),
                  )
            );
            $view_model->getView('utilities_list', $data);
        } else if ($action = 'faqs') {
            $view_model->getView('faqs');
        } else {
            $view_model->getView('home');
        }
            
        $view_model->getView("footer");

    }


}
