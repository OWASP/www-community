## Host Chapters by Hour
*all times UTC - hover over link for local time*

### Saturday
* [12:00 - 13:00 - **Opening Session**]()
* [13:00 - 14:00 - Belgium](/www-chapter-belgium/)
* [14:00 - 15:00 - New York City](https://wiki.owasp.org/index.php/New_York_City) (NY, USA) 
* [15:00 - 16:00 - Uruguay](/www-chapter-uruguay/)
* [16:00 - 17:00 - Chile](/www-chapter-chile/)
* [17:00 - 18:00 - Cairo](/www-chapter-cairo/) (Egypt)
* [18:00 - 19:00 - Guatemala](/www-chapter-guatemala/)
* [19:00 - 20:00 - Atlanta](/www-chapter-atlanta/) (GA, USA)
* [20:00 - 21:00 - Orange County](/www-chapter-orange-county/) (CA, USA)
* [21:00 - 22:00 - Santa Barbara](/www-chapter-santa-barbara/) (CA, USA)
* [22:00 - 23:00 - Hawaii](https://wiki.owasp.org/index.php/Hawaii) (USA)
* [23:00 - 00:00 - Viña del Mar](/www-chapter-vina-del-mar/) (Chile)

### Sunday
* [00:00 - 01:00 - New Zealand](/www-chapter-new-zealand/)
* [01:00 - 02:00 - Victoria](/www-chapter-victoria/) (BC, Canada)
* [02:00 - 03:00 - Japan](/www-chapter-japan/) (Japan)
* [03:00 - 04:00 - Melbourne](/www-chapter-melbourne/) (Australia)
* [04:00 - 04:55 - Bangalore](/www-chapter-bangalore/) (India)
* [04:55 - 05:15 - Jakarta](/www-chapter-jakarta/) (Indonesia)
* [05:15 - 06:10 - Kerala](/www-chapter-kerala/) (India)
* [06:10 - 07:05 - Nagpur](/www-chapter-nagpur/) (India)
* [07:05 - 08:00 - Meerut](/www-chapter-meerut/) (India)
* [08:00 - 09:00 - Israel](/www-chapter-israel/)
* [09:00 - 10:00 - Kyiv](/www-chapter-kyiv/) (Ukraine)
* [10:00 - 11:00 - Cambridge](/www-chapter-cambridge/) (UK)
* [11:00 - 12:00 - London](/www-chapter-london/) (UK)
* [12:00 - 12:30 - **Closing Remarks**]()



<script type='text/javascript'>
  $(function(){
    $("a").hover(function() {
      utc_str = $(this).text();
      ndx = utc_str.indexOf(':');
     
      if(ndx >= 0)
      {
        st_hour_str = utc_str.substring(0, ndx);
        st_min_str = utc_str.substring(ndx + 1, ndx + 3);
        // get utc time, 24 hour format...
        utc_dt = luxon.DateTime.utc(2020, 06, 06, parseInt(st_hour_str), parseInt(st_min_str), 0);
        start_dt = utc_dt.setZone(luxon.DateTime.local().zoneName);

        ndx = utc_str.lastIndexOf(':');
        end_hour_str = utc_str.substring(ndx - 2, ndx);
        end_min_str = utc_str.substring(ndx + 1, ndx + 3);
        
        utc_dt = luxon.DateTime.utc(2020, 06, 06, parseInt(end_hour_str), parseInt(end_min_str), 0);
        end_dt = utc_dt.setZone(luxon.DateTime.local().zoneName);
        popstr = start_dt.toLocaleString(luxon.DateTime.TIME_24_SIMPLE) + ' to ' + end_dt.toLocaleString({ hour: '2-digit', minute: '2-digit', hour12: false, timeZoneName: 'short' });
        $(this).prop('title', popstr);
      }
    });
  });

  
</script>
