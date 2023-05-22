    axes = plt.axes()
    plt.plot(heures, distances)
    gares = ['Roanne', 'Feurs', 'Saint Just Saint Rambert', 'Saint Etienne']
    heures = ['6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    axes.set_yticks([0, 42, 74, 88])
    axes.set_xticks([k*60 for k in range(18)])
    axes.set_yticklabels(gares)
    axes.set_xticklabels(heures)
    plt.xlim(0,17*60)
    plt.xticks(rotation = 90)
    plt.show()
    time.sleep(1)
    plt.close()