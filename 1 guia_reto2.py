def cliente (informacion:dict) -> dict:
      datos = dict()
      edad = informacion['edad']
      apto = True
      if edad > 18:
       atraccion = 'X-Treme'
      valor_boleta = 20000
      if informacion['primer_ingreso']:
       valor_boleta = valor_boleta * 0.95
      elif edad >= 15 and edad <= 18:
       atraccion = 'Carros chocones'
      valor_boleta = 5000
      if informacion['primer_ingreso']:
        valor_boleta = valor_boleta * 0.93
      elif edad >= 7 and edad < 15:
       atraccion = 'Sillas voladoras'
      valor_boleta = 10000
      if informacion['primer_ingreso']:
       valor_boleta = valor_boleta * 0.95
      else:
       apto = False
      atraccion = 'N/A'
      valor_boleta = 'N/A'

      datos['nombre'] = informacion['nombre']
      datos['edad'] = informacion['edad']
      datos['atraccion'] = atraccion
      datos['apto'] = apto
      datos['primer_ingreso'] = informacion['primer_ingreso']
      datos['total_boleta'] = valor_boleta

      return datos