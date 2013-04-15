<?php

require_once 'models/view.php';

class User {

    function get($pairs, $data = '') {

        if (empty($pairs['action'])) {
            $action = 'home';
        } else {
            $action = $pairs['action'];
        }

        $data = array( 'username' => 'tbsmith' );
        if ($action == 'home') {
            $this->getUserHome($data);
        } else if ($action == 'start-edit') {
            $this->startEdit($data);
        } else if ($action == 'perform-edit') {
            $this->performEdit($data);
            $this->getUserHome($data);
        } else if ($action == 'login') {
            $this->login($data);
        } else if ($action == 'register') {
            $this->register($data);
        } else if ($action == 'perform-register') {
            $this->performRegister($pairs, $data);
        } else {
            $this->getUserHome($data);
        }

    }

    function getUserHome($data) {
        $view_model = new View();
        $view_model->getView('header', $data);
        $view_model->getView('navbar', $data);
        $view_model->getView('user_home', $data);
        $view_model->getView('footer', $data);
    }

    function startEdit($data) {
    }

    function performEdit($data) {
    }

    function performRegister($data) {
        $view_model = new View();
        $view_model->getView('header', $data);
        $view_model->getView('navbar', $data);

        // is the info verified?
        //   show thanks and welcome page
        // else
        //   populate errors and show register page

        $view_model->getView('register', $data);
        $view_model->getView('footer', $data);
    }

    function register($data) {
        $view_model = new View();
        $view_model->getView('header', $data);
        $view_model->getView('navbar', $data);
        $view_model->getView('register', $data);
        $view_model->getView('footer', $data);
    }

    function login($data) {
        $view_model = new View();
        $view_model->getView('header', $data);
        $view_model->getView('navbar', $data);
        $view_model->getView('login', $data);
        $view_model->getView('footer', $data);
    }

}
