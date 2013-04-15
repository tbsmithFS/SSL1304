<?php

/*
    This is our main interface for the user
    for handling the displaying of static pages
*/

require_once 'models/view.php';

class Home {
    function get($pairs, $data = '') {

        if (empty($pairs['action'])) {
            $action = 'home';
        } else {
            $action = $pairs['action'];
        }

        $view_model = new View();
        $view_model->getView("header");

        $data = array('bottomLeftContent' => "hi BL",
                      'bottomRightContent' => "hi BR"
                      );

        if ($action == 'home') {
            $view_model->getView('home', $data);
        } else if ($action == 'contact') {
            $view_model->getView('contact', $data);
        } else if ($action == 'faqs') {
            $view_model->getView('faqs', $data);
        } else {
            $view_model->getView('home', $data);
        }

        $view_model->getView("footer", $data);

    }


}



