
def heikin_ashi_candles ( open, high, low, close ):

      ha_close =  np.empty(len(close), dtype=np.float32 )

      ha_high = np.empty(len(close), dtype=np.float32 )
      ha_low  = np.empty(len(close), dtype=np.float32 )
      ha_open = np.empty(len(close), dtype=np.float32 )

      # candles =  np.empty(len(close) , dtype='U10')
      # candles = [[]] *  len(close) , dtype=np.int16

      ha_open[0]  = (open[0] + close[0] ) /2
      ha_close[0] = (close[0] + open[0] + high[0] + low[0]) /4

      for i in range(1 , len(close) ):
            ha_open[i]  = (ha_open[i-1] + ha_close[i-1] ) / 2
            ha_close[i] = (open[i] +  high[i] + low[i] + close[i]) / 4
            ha_high[i]  = max( high[i], ha_open[i], ha_close[i]  )
            ha_low[i]   = min( low[i], ha_open[i], ha_close[i]  )

      return   ha_open, ha_close, ha_high, ha_low



  
def heikin_ashi_status( ha_open , ha_close ):

      candles =  np.full_like( ha_close, '', dtype='U10')

      for i in range(1 , len(ha_close) ):

            # green_condition =  ha_close[i] > ha_open[i]
            # red_condition   =  ha_close[i] < ha_open[i]
            if ha_close[i] > ha_open[i] :
              candles[i]  = 'Green'

            elif ha_close[i] < ha_open[i] :
              candles[i]  = 'Red'
            else:
              candles[i] = 'Neutral'

      return  candles


  
