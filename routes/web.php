<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('home.index');
});


Route::get('/article/auto-lenders', function () {
    return view('article.auto-lender');
});