import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'Screens/Homepage.dart';
import 'Tools/ImageShifter.dart';
import 'Models/Image.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
        body: ChangeNotifierProvider<BackImage>(
          create: (_) => BackImage(
              Container(
                decoration: BoxDecoration(
                    image: DecorationImage(
                        image: AssetImage('img/ImageDelhi.jpg'),
                        fit: BoxFit.fill)),
              ),
              "Delhi",
              "A city is a large human settlement"),
          child: Stack(
            children: [
              ImageShifter(),
              HomeShelf(),
            ],
          ),
        ),
      ),
    );
  }
}
