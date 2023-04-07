import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from decimal import Decimal


class PRPlot():
    def __int__(self, ms=30, lw=3, name_plot=None, x_name="X", y_name="Y",save_name="Plot"):
        self.ms = ms
        self.lw = lw
        self.name_plot = name_plot
        self.x_name = x_name
        self.y_name = y_name
        self.save_name = save_name

    def my_round(self,step,ma,mi,num,str):
        lis = list()
        lis_n=list()
        step = round(step, num)
        start = math.floor(mi / step)
        for i in range(start, start + 18):
            s = i * step
            lis.append(Decimal(s).quantize(Decimal(str)))
            lis_n.append(s)
            if s >= ma:
                break
        return lis,lis_n
    
    def ax(self, array):
        ma=max(array)
        mi=min(array)
        delta=(ma-mi)
        step=delta/6
        if delta<=0.5:
            return self.my_round(step,ma,mi,2,"1.01")
        if delta >0.5 and delta < 5:
            return self.my_round(step, ma, mi, 1, "1.1")
        if delta >=5 and delta <= 15:
            return self.my_round(step, ma, mi, 0, "1")

    def n_dat(self,arr1,arr2):
        lis=list()
        for i in arr1:
            lis.append(i)
        for i in arr2:
            lis.append(i)
        return lis

    def main(self, ref, predict, save):
        # mpl.rc('font', family='Times New Roman')
        fig, axs = plt.subplots(figsize=(12, 7))
        axs.plot(ref, predict, ".", color="red", ms=self.ms)
        axs.plot(ref, ref, color="blue", lw=self.lw)

        lis_x, lis_x_num = self.ax(ref)
        lis_y, lis_y_num = self.ax(self.n_dat(ref,predict))

        axs.set_xticks(lis_x_num)
        axs.set_yticks(lis_y_num)

        axs.set_ylabel(self.y_name, fontsize=25, labelpad=8)
        axs.grid(color="black", linewidth=0.7)
        axs.set_xlabel(self.x_name, fontsize=25, labelpad=15)
        axs.set_title(self.name_plot, fontsize=28, loc="center", pad=15)
        axs.tick_params(which='major', length=10, width=2)

        axs.set_xticklabels(lis_x, fontsize=20)
        axs.set_yticklabels(lis_y, fontsize=20)

        axs.get_xaxis().set_tick_params(direction='in')
        axs.get_yaxis().set_tick_params(direction='in')

        if save:
            plt.savefig(self.save_name+'.png', format='png', dpi=300)
            plt.savefig(self.save_name+".svg", format="svg")
        plt.show()
        return 0
