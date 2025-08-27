import 'package:flutter/material.dart';
import 'package:fpv_blackbox/screens/upload_screen.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FPV Analyzer',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: UploadScreen(),
    );
  }
}