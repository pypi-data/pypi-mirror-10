QuantDigger
============
QuantDigger����һȺ�������װ�����һ�𿪷��Ŀ�Դ�Ĺ�Ʊ/�ڻ��ز���
��Ҫ����ѧϰ���о�����ӭ����ṩ������������״���ޣߣޣ�
���߼������ǵ�python��������Ⱥ--334555399��

���˿�����Ա����Ҫ�ر��л vodkabuaa_ �����������
ongbe_ ��æ�޸�����bug�� tushare������� Jimmy_ ���Լ��������ѵ�֧�֣�

**��Ҫ���빱����:**
     deepfish_

     TeaEra_

     wondereamer_

     HonePhy_

��װ
----
    
�����ѡ��pip��װ
   
  ::
       
      python install_pip.py  (����Ѿ���װ��pip,�Թ���һ����)
      pip install QuantDigger
      python install_dependency.py

���߿�¡github����󱾵ذ�װ
   
  ::
       
      git clone https://github.com/QuantFans/quantdigger.git
      python install.py  (����������װpip, ��������)


������
------
* Python 
* pandas 
* python-dateutil 
* matplotlib 
* numpy
* TA-Lib
* logbook
* pyqt (��ѡ)
* tushare_ (��ѡ, һ���ǳ�ǿ��Ĺ�Ʊ��Ϣץȡ����)

����DEMO
--------
Դ��
~~~~
.. code:: py

    from quantdigger.kernel.engine.execute_unit import ExecuteUnit
    from quantdigger.kernel.indicators.common import MA, BOLL
    from quantdigger.kernel.engine.strategy import TradingStrategy, pcontract, stock
    import plotting


    class DemoStrategy(TradingStrategy):
        """ ������ """
        def __init__(self, pcontracts, exe):
            """ ��ʼ��ָ����� """
            super(DemoStrategy, self).__init__(pcontracts, exe)

            self.ma20 = MA(self, self.close, 20,'ma20', 'b', '1')
            self.ma10 = MA(self, self.close, 10,'ma10', 'y', '1')
            self.b_upper, self.b_middler, self.b_lower = BOLL(self, self.close, 10,'boll10', 'y', '1')
            #self.ma2 = NumberSeries(self)

        def on_tick(self):
            """ ���Ժ�������ÿ��Bar����һ�Ρ�""" 
            #self.ma2.update(average(self.open, 10))
            if self.ma10[1] < self.ma20[1] and self.ma10 > self.ma20:
                self.buy('d', self.open, 1) 
            elif self.position() > 0 and self.ma10[1] > self.ma20[1] and self.ma10 < self.ma20:
                self.sell('d', self.open, 1) 

            print self.position(), self.cash()
            print self.datetime, self.b_upper, self.b_middler, self.b_lower


    # ���в���
    begin_dt, end_dt = None, None
    pcon = pcontract('SHFE', 'IF000', 'Minutes', 10)
    #pcon = stock('600848')  ����tushareԶ�̼��ع�Ʊ����
    simulator = ExecuteUnit(begin_dt, end_dt)
    algo = DemoStrategy([pcon], simulator)
    simulator.run()

    # ��ʾ�ز���
    plotting.plot_result(simulator.data[pcon],
                algo._indicators,
                algo.blotter.deal_positions,
                algo.blotter)


���Խ��
~~~~~~~~
**main.py**

* k�ߺ��ź���

  .. image:: figure_signal.png
     :width: 500px

* �ʽ����ߡ�
  
  .. image:: figure_money.png
     :width: 500px

����
~~~~~~~~
**mplot_demo.py  matplotlib��k�ߣ�ָ���ߵ�demo��**
  .. image:: plot.png
     :width: 500px

**pyquant.py ����pyqt�� ������ipython��matplotlib��demo��**
  .. image:: pyquant.png
     :width: 500px

.. _TeaEra: https://github.com/TeaEra
.. _deepfish: https://github.com/deepfish
.. _wondereamer: https://github.com/wondereamer
.. _HonePhy: https://github.com/HonePhy
.. _tushare: https://github.com/waditu/tushare
.. _Jimmy: https://github.com/jimmysoa
.. _vodkabuaa: https://github.com/vodkabuaa
.. _ongbe: https://github.com/ongbe
