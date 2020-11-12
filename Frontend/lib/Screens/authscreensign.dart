import 'dart:async';
import 'dart:html';

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/Auth.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Screens/HomePage.dart';
import 'package:travel/Screens/SearchScreen.dart';
import 'package:http/http.dart';

class AuthScreenSign extends StatefulWidget {
  final Function signin;

  AuthScreenSign({this.signin});

  @override
  _AuthScreenSignState createState() => _AuthScreenSignState();
}

class _AuthScreenSignState extends State<AuthScreenSign> {
  String username = "";
  String fullname = "";
  String email = "";
  String password = "";
  String phone = "";

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    final _key = GlobalKey<FormState>();
    return Container(
      padding: EdgeInsets.symmetric(
          vertical: _screenSize.width * 0.05,
          horizontal: _screenSize.height * 0.15),
      child: Column(
        children: [
          Container(
            margin: EdgeInsets.symmetric(vertical: 5),
            alignment: Alignment.topLeft,
            child: RaisedButton(
              padding: EdgeInsets.symmetric(vertical: 15, horizontal: 10),
              color: Colors.deepPurpleAccent,
              onPressed: () {
                widget.signin(false);
              },
              child: Text(
                "Login",
                style: GoogleFonts.raleway(color: Colors.white, fontSize: 16),
              ),
            ),
          ),
          SizedBox(
            height: _screenSize.height * 0.05,
          ),
          Container(
            alignment: Alignment.centerLeft,
            margin: EdgeInsets.only(left: _screenSize.width * 0.14),
            padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
            child: RaisedButton(
                padding: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      FontAwesomeIcons.google,
                      color: Colors.white,
                      size: 14,
                    ),
                    SizedBox(width: 40),
                    Text(
                      "Sign Up with Google",
                      style: GoogleFonts.raleway(
                          color: Colors.white, fontSize: 18),
                    ),
                    SizedBox(width: 40),
                  ],
                ),
                color: Colors.blue,
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => HomePage()));
                }),
          ),
          SizedBox(
            height: _screenSize.height * 0.01,
          ),
          Container(
            margin: EdgeInsets.only(right: _screenSize.width * 0.16),
            width: _screenSize.width * 0.4,
            alignment: Alignment.topLeft,
            child: Form(
              key: _key,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Container(
                        padding:
                            EdgeInsets.symmetric(vertical: 2, horizontal: 8),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(10),
                          color: Color(0xffE8E8E8),
                        ),
                        width: 200,
                        child: TextFormField(
                          style: GoogleFonts.raleway(
                              color: Colors.black, fontWeight: FontWeight.w500),
                          cursorColor: Colors.black,
                          decoration: InputDecoration(
                            hintText: "Username",
                            hintStyle: GoogleFonts.raleway(
                                color: Colors.black,
                                fontWeight: FontWeight.w500),
                            border: InputBorder.none,
                          ),
                          onSaved: (val) => username = val,
                        ),
                      ),
                      SizedBox(
                        width: 60,
                      ),
                      Container(
                        padding:
                            EdgeInsets.symmetric(vertical: 2, horizontal: 8),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(10),
                          color: Color(0xffE8E8E8),
                        ),
                        width: 200,
                        child: TextFormField(
                          style: GoogleFonts.raleway(
                              color: Colors.black, fontWeight: FontWeight.w500),
                          cursorColor: Colors.black,
                          decoration: InputDecoration(
                            hintText: "Full Name",
                            hintStyle: GoogleFonts.raleway(
                                color: Colors.black,
                                fontWeight: FontWeight.w500),
                            border: InputBorder.none,
                          ),
                          onSaved: (val) => fullname = val,
                        ),
                      )
                    ],
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  Container(
                    padding: EdgeInsets.symmetric(vertical: 2, horizontal: 8),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      color: Color(0xffE8E8E8),
                    ),
                    width: 460,
                    child: TextFormField(
                      style: GoogleFonts.raleway(
                          color: Colors.black, fontWeight: FontWeight.w500),
                      cursorColor: Colors.black,
                      decoration: InputDecoration(
                        hintText: "Phone Number",
                        hintStyle: GoogleFonts.raleway(
                            color: Colors.black, fontWeight: FontWeight.w500),
                        border: InputBorder.none,
                      ),
                      onSaved: (val) => phone = val,
                    ),
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  Container(
                    padding: EdgeInsets.symmetric(vertical: 2, horizontal: 8),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      color: Color(0xffE8E8E8),
                    ),
                    width: 460,
                    child: TextFormField(
                      style: GoogleFonts.raleway(
                          color: Colors.black, fontWeight: FontWeight.w500),
                      cursorColor: Colors.black,
                      decoration: InputDecoration(
                        hintText: "Email ID",
                        hintStyle: GoogleFonts.raleway(
                            color: Colors.black, fontWeight: FontWeight.w500),
                        border: InputBorder.none,
                      ),
                      onSaved: (val) => email = val,
                    ),
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  Container(
                    padding: EdgeInsets.symmetric(vertical: 2, horizontal: 8),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      color: Color(0xffE8E8E8),
                    ),
                    width: 460,
                    child: TextFormField(
                      style: GoogleFonts.raleway(
                          color: Colors.black, fontWeight: FontWeight.w500),
                      cursorColor: Colors.black,
                      obscureText: true,
                      decoration: InputDecoration(
                        hintText: "Password",
                        hintStyle: GoogleFonts.raleway(
                            color: Colors.black, fontWeight: FontWeight.w500),
                        border: InputBorder.none,
                      ),
                      onSaved: (val) => password = val,
                    ),
                  ),
                  SizedBox(
                    height: _screenSize.height * 0.03,
                  ),
                  RaisedButton(
                    onPressed: () {
                      _key.currentState.save();
                      showDialog(
                          context: context,
                          builder: (context) {
                            Widget center = CircularProgressIndicator();
                            String text = "Making Account";
                            return Dialog(
                              child: Consumer<User>(
                                builder: (context, user, child) {
                                  return Column(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      FutureBuilder(
                                          future: AuthService.register(email, username, phone,
                                              password, fullname),
                                          builder: (context, snapshot) {
                                            if (snapshot.hasData) {
                                              Response response = snapshot.data;
                                              print(response.body);
                                              if (response.statusCode == 201) {
                                                user.populateUserRegister(response.body);
                                                  center = Icon(
                                                    Icons.check,
                                                    color: Colors.green,
                                                  );
                                                  text = "Account Created !!";
                                                Timer timer =
                                                    new Timer(Duration(seconds: 2), () {
                                                  Navigator.push(
                                                      context,
                                                      MaterialPageRoute(
                                                          builder: (context) =>
                                                              HomeScreen()));
                                                });
                                              }
                                            }
                                            return Column(
                                              children: [
                                                center,
                                                Text(text),
                                              ],
                                            );
                                          }),
                                    ],
                                  );
                                }
                              ),
                            );
                          });
                    },
                    color: Color(0xffb8e6f5),
                    child: Text(
                      "Sign Up",
                      style: GoogleFonts.raleway(
                          color: Color(0xff3489bb),
                          fontWeight: FontWeight.w700),
                    ),
                  )
                ],
              ),
            ),
          )
        ],
      ),
    );
  }
}
