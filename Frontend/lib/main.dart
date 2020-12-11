import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:travel/Models/Monument.dart';
import 'package:travel/Models/User.dart';
import 'Models/City.dart';
import 'Screens/LandingPage.dart';
import 'Tools/ImageShifter.dart';
import 'Models/Image.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider<User>(create: (_) => User()),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            primaryColor: Color(0xff577399),
            accentColor: Color(0xffFE5F55),
            primaryColorLight: Color(0xffBDD5EA),
            primaryColorDark: Color(0xff495867),
            backgroundColor: Color(0xffF7F7FF),
            scaffoldBackgroundColor: Colors.white,
            fontFamily: 'Raleway'),
        home: Scaffold(
          backgroundColor: Colors.black,
          body: ChangeNotifierProvider<BackImage>(
            create: (_) => BackImage(
                Container(
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.only(
                        topRight: Radius.circular(20),
                        bottomRight: Radius.circular(20),
                      ),
                      image: DecorationImage(
                          image: AssetImage('img/ImageDelhi.jpg'),
                          fit: BoxFit.fill)),
                ),
                "Delhi",
                "A city is a large human settlement"),
            child: Stack(
              children: [
                ImageShifter(
                  xOffset: -1.0,
                  yOffset: 0.0,
                ),
                HomeShelf(),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
