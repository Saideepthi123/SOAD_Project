import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_datepicker/datepicker.dart';

class GuideFilter extends StatelessWidget {
  double width;
  GuideFilter({this.width});
  @override
  Widget build(BuildContext context) {
    return Container(
      width: width,
      child: Row(
        children: [
          Container(
            height: width,
            width: width,
            child: SfDateRangePicker(
              onSelectionChanged: (val){

              },
              selectionMode: DateRangePickerSelectionMode.range,
            ),
          )
        ],
      ),
    );
  }
}
