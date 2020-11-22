import 'package:flutter/material.dart';

class CityTravelTab extends StatefulWidget {
  @override
  _CityTravelTabState createState() => _CityTravelTabState();
}

class _CityTravelTabState extends State<CityTravelTab> {
  @override
  Widget build(BuildContext context) {
    final _screenSize=MediaQuery.of(context).size;
    return Container(
      child: ListView(
        shrinkWrap: true,
        children: [
          Card(
            elevation: 10,
            child: Container(
              // alignment: Alignment.topRight,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Container(
                    padding: EdgeInsets.all(10),
                    width: _screenSize.width*0.1,
                    child: TextField(),
                  ),
                  Container(
                    padding: EdgeInsets.all(10),
                    width: _screenSize.width*0.1,
                    child: TextField(),
                  ),
                  IconButton(
                    icon: Icon(Icons.calendar_today_outlined),
                    onPressed: (){
                      showDatePicker(
                          context: context,
                          initialDate: DateTime.now(),
                          firstDate: DateTime.now(),
                          lastDate: DateTime(2022)
                      ).then((date) {
                        if(date!=null){
                          print(date);
                        }
                      });
                    },
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
