import 'dart:ui';

import 'package:flutter/material.dart';
import 'home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "TO DO LIST",
      theme: ThemeData(
          primarySwatch: Colors.red,
          textTheme: TextTheme(
            headline1: TextStyle(
              fontSize: 30.0,
              fontWeight: FontWeight.w500,
              color: Color.fromARGB(255, 8, 8, 8),
            ),
          )),
      home: HomePage(),
    );
  }
}
