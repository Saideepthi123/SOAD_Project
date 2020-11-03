import 'authscreensign.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'authlog.dart';

class LogIn extends StatefulWidget {
  @override
  _LogInState createState() => _LogInState();
}

class _LogInState extends State<LogIn> with SingleTickerProviderStateMixin {
  bool signin = false;
  bool change = true;
  AnimationController _controller;
  Animation<Color> _animation;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _controller =
        AnimationController(vsync: this, duration: Duration(milliseconds: 300));
    _animation = ColorTween(
      begin: Color(0xffb8e6f5),
      end: Color(0xfffcc340),
    ).animate(_controller)
      ..addListener(() {
        if (_controller.value > 0.5 )
          setState(() {
            change = false;
          });
        else
          setState(() {
            change = true;
          });
      });
  }

  SetsignIn(bool set) {
    setState(() {
      signin = set;
    });
    (!signin)
        ? _controller.animateBack(0, curve: Curves.ease)
        : _controller.animateTo(1, curve: Curves.ease);
  }

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    return Scaffold(
      body: Card(
          elevation: 10,
          margin: EdgeInsets.symmetric(
              horizontal: _screenSize.width * 0.05,
              vertical: _screenSize.width * 0.03),
          shape:
          RoundedRectangleBorder(borderRadius: BorderRadius.circular(60)),
          child: Stack(
            children: [
              Container(
                height: _screenSize.height * 0.96,
                width: _screenSize.width * 0.9,
                child: Stack(
                  children: [
                    AnimatedPositioned(
                      left: signin ? _screenSize.width * 0.6 : 0,
                      duration: Duration(milliseconds: 700),
                      child: Container(
                        alignment: Alignment.topCenter,
                        padding:
                        EdgeInsets.symmetric(vertical: 20, horizontal: 50),
                        width: _screenSize.width * 0.3,
                        height: _screenSize.height * 0.94,
                        color: _animation.value,
                        child: (change)
                            ? Column(
                          mainAxisSize: MainAxisSize.max,
                          mainAxisAlignment:
                          MainAxisAlignment.spaceAround,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              "Login",
                              style: GoogleFonts.raleway(
                                  color: Color(0xff3498DB),
                                  fontWeight: FontWeight.w900,
                                  fontSize: 36),
                            ),
                            Text(
                              "To meet people around the globe",
                              style: GoogleFonts.raleway(
                                  color: Color(0xff3498DB),
                                  fontWeight: FontWeight.w500,
                                  fontSize: 36),
                            ),
                            Image.asset(
                              'img/air.png',
                              width: _screenSize.width * 0.25,
                              fit: BoxFit.contain,
                            )
                          ],
                        )
                            : Column(
                          mainAxisSize: MainAxisSize.max,
                          mainAxisAlignment:
                          MainAxisAlignment.spaceAround,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              "Sign Up",
                              style: GoogleFonts.raleway(
                                  color: Color(0xff3498DB),
                                  fontWeight: FontWeight.w900,
                                  fontSize: 36),
                            ),
                            Text(
                              "To connect with people around the globe",
                              style: GoogleFonts.raleway(
                                  color: Color(0xff3498DB),
                                  fontWeight: FontWeight.w500,
                                  fontSize: 36),
                            ),
                            Image.asset(
                              'img/scooter.png',
                              width: _screenSize.width * 0.25,
                              fit: BoxFit.contain,
                            )
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                  alignment: Alignment.topRight,
                  child: (change)
                      ? AuthScreenLogin(signin: SetsignIn)
                      : AuthScreenSign(signin: SetsignIn)),
            ],
          )),
    );
  }
}