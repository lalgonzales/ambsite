<?php
// Archivo de rutas mínimo para Laravel

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});
