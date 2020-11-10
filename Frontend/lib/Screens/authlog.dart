import 'dart:async';
import 'dart:html';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:travel/APIcalls/Auth.dart';
import 'package:travel/Models/User.dart';
import 'package:travel/Screens/HomePage.dart';

class AuthScreenLogin extends StatefulWidget {
  final Function signin;

  AuthScreenLogin({this.signin});

  @override
  _AuthScreenLoginState createState() => _AuthScreenLoginState();
}

class _AuthScreenLoginState extends State<AuthScreenLogin> {
  String email = "";
  String password = "";

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    final _key = GlobalKey<FormState>();
    return Container(
      alignment: Alignment.topRight,
      padding: EdgeInsets.symmetric(
          vertical: _screenSize.width * 0.05,
          horizontal: _screenSize.height * 0.15),
      width: _screenSize.width * 0.6,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          Container(
            alignment: Alignment.topRight,
            child: RaisedButton(
              padding: EdgeInsets.symmetric(vertical: 20, horizontal: 10),
              color: Colors.deepPurpleAccent,
              onPressed: () {
                widget.signin(true);
              },
              child: Text(
                "Sign Up",
                style: GoogleFonts.raleway(color: Colors.white, fontSize: 16),
              ),
            ),
          ),
          SizedBox(
            height: _screenSize.height * 0.05,
          ),
          Container(
            alignment: Alignment.centerRight,
            margin: EdgeInsets.only(right: _screenSize.width * 0.14),
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
                      "Login with Google",
                      style: GoogleFonts.raleway(
                          color: Colors.white, fontSize: 18),
                    ),
                    SizedBox(width: 40),
                  ],
                ),
                color: Colors.blue,
                onPressed: () {
                  print("Daba mat na");
                }),
          ),
          SizedBox(
            height: _screenSize.height * 0.05,
          ),
          Container(
            margin: EdgeInsets.only(left: _screenSize.width * 0.08),
            width: _screenSize.width * 0.4,
            alignment: Alignment.topRight,
            child: Form(
              key: _key,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    margin: EdgeInsets.only(right: 100),
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
                      onSaved: (val) => email = val.trim(),
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
                    height: _screenSize.height * 0.05,
                  ),
                  RaisedButton(
                    onPressed: () async {
                      _key.currentState.save();
                      showDialog(
                          context: context,
                          builder: (context) {
                            Widget center = CircularProgressIndicator();
                            // add some zing to it, you're a writer what the hell
                            String text = "Logging you in";
                            return Dialog(
                              child: Consumer<User>(
                                builder: (context, user, child) {
                                  return FutureBuilder(
                                      future: AuthService.login(email,
                                          password),
                                      builder: (context, snapshot) {
                                        if (snapshot.hasData) {
                                          Response response = snapshot.data;
                                          if (response.statusCode == 200) {
                                            print(response.headers['set-cookie']);
                                            user.populateUserLogin(response.body);
                                            center = Icon(
                                              Icons.check,
                                              color: Colors.green,
                                            );
                                            Timer timer =
                                            new Timer(Duration(seconds: 2), () {
                                              Navigator.push(
                                                  context,
                                                  MaterialPageRoute(
                                                      builder: (context) =>
                                                          HomePage()));
                                            });
                                          }
                                        }
                                        return Column(
                                          children: [
                                            center,
                                            Text(text),
                                          ],
                                        );
                                      });
                                }
                              ),
                            );
                          });
                    },
                    color: Color(0xffb8e6f5),
                    child: Text(
                      "Login",
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
