import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:consumerapp1/Models/Guide.dart';

class GuideFilter extends StatelessWidget {
  double width;
  String dropdownValue = "Pay by hour";
  Function onDone;
  GuideFilter({this.width,this.onDone});

  bool ed=false,sd=false,type=false;
  @override
  Widget build(BuildContext context) {
    final bookGuide=Provider.of<BookGuide>(context);
    return Container(
      padding: EdgeInsets.all(5),
      width: width,
      child: Card(
        elevation: 10,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Text("Start Date: "),
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
                    bookGuide.updateStartDate(date);
                    sd=true;
                  }
                });
              },
            ),
            Text("End Date: "),
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
                    bookGuide.updateEndDate(date);
                    ed=true;
                  }
                });
              },
            ),
            IconButton(
              icon: Icon(Icons.search,size: 30,),
              onPressed: onDone,
            )
          ],
        ),
      ),
    );
  }
}
