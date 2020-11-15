import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:travel/APIcalls/Auth.dart';
import 'package:travel/Screens/City.dart';
import 'package:travel/Screens/SearchScreen.dart';
import 'package:travel/Screens/loginSign.dart';
import '../Screens/HomePage.dart';

class TopAppBar extends AppBar {
  BuildContext context;

  @override
  // TODO: implement leading
  Widget get leading => IconButton(
        icon: Icon(FontAwesomeIcons.plane),
        onPressed: () {
          Navigator.push(
              context, MaterialPageRoute(builder: (context) => HomeScreen()));
        },
      );

  @override
  Widget get title => InkWell(
      onTap: () {
        Navigator.push(
            context, MaterialPageRoute(builder: (context) => CityPage()));
      },
      child: Text("Hello"));

  @override
  List<Widget> get actions => [
        RaisedButton(
          child: Text("Logout"),
          onPressed: () {
            AuthService.logout().then((value) {
              print(value.body);
                  Navigator.pushAndRemoveUntil(
                      context,
                      MaterialPageRoute(builder: (context) => LogIn()),
                      (route) => false);
                });
          },
        )
      ];
  TopAppBar(this.context);
}


class SearchBar extends StatelessWidget {
  List<String> suggestions;
  double width;
  Function onChange;
  SearchBar({this.suggestions,this.width,this.onChange});
  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 10,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(50),
      ),
      child: Container(
        padding: EdgeInsets.all(8),
        height: 50,
        child: Row(
          children: [
            Icon(Icons.search),
            SizedBox(width: 8,),
            Container(
              width: width*0.8,
              padding: EdgeInsets.only(bottom: 10),
              child: TextField(
                autofillHints: suggestions,
                enableSuggestions: true,
                decoration: InputDecoration(
                  border: InputBorder.none,
                ),
                onTap: () {},
                onChanged: onChange,
              ),
            )
          ],
        ),
      ),
    );
  }
}
