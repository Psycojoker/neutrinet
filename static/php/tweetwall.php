<?php

date_default_timezone_set('Europe/Brussels');

function getTweetWall ($maxItems = 5) {
  global $tweetWall;

  $target = 'https://identi.ca/api/statuses/user_timeline/292360.rss';

  $referers = array('http://google.com', 'http://yahoo.com', 'http://bing.com', 'http://duckduckgo.com', 'http://seeks.fr', 'http://twitter.com', 'http://facebook.com');
  $userAgents = array(
    'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko Firefox/11.0',
    'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
    'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
    'Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)');

  $referer = $referers[rand(0, count($referers) - 1)];
  $userAgent = $userAgents[rand(0, count($userAgents) - 1)];

  $ch = curl_init();

  curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);
  curl_setopt($ch, CURLOPT_URL, $target);
  curl_setopt($ch, CURLOPT_FAILONERROR, true);
  curl_setopt($ch, CURLOPT_REFERER, $referer);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $res = curl_exec($ch);

  curl_close($ch);

  if ($res) {
    $feed = new SimpleXMLElement($res);

    foreach ($feed->channel->item as $item) {
      $i++;

      if ($i <= $maxItems)
      {
        $tweet = preg_replace(
          array(
            '!^(?:neutrinet: )!i',
            '!((?:(?:(?:(?:(?:ht|f)tps?)|mms):(?://))|www)+[\w\d:#@%/;$()~_?\+-=\.&]*)!i',
            '! (@([\w]*))!i'
          ),
          array(
            '',
            "<a href='$1'>$1</a> ",
            " <a href='https://twitter.com/$2'>$1</a>"
          ), $item->title);

        $tweetWall[$i]['tweet'] = $tweet;
        $tweetWall[$i]['date'] = date('Y/m/d H:i:s', strtotime($item->pubDate));
      }
    }
  }
  else {
    $tweetWall = 'Error: unable to fetch RSS feed.';
  }
}

getTweetWall();

if (is_array($tweetWall))
{
  echo '<ul>';
  foreach($tweetWall as $key => $item) { echo '<li><span class="tweet">' . $item['tweet'] . '</span> <span class="date">' . $item['date'] . '</span></li>'; }
  echo '</ul>';
}
else {
  echo '<p>' . $tweetWall . '</p>';
}

?>