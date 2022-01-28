"""
Source: http://barcode128.blogspot.com/2007/03/code128py.html

This class generate code 128 (http://en.wikipedia.org/wiki/Code_128) bar code, 
it requires PIL (python imaging library) installed.

This program is based on EanBarCode.py found on 
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/426069 submitted by Remi Inconnu.

Code 128 is variable lenght and a 103 module checksum is added automatically.

Create bar code sample :
   from Code128 import Code128
   bar = Code128()
   bar.getImage("9782212110708",50,"gif")
"""

# courbB08.pil PIL Font file uuencoded
courB08_pil ="""eJztl91rFkcUxp+Zt7vGFYzVtiJKICgYlLRWkaBBVGgDraFGCH5gsQp+QMBqabAVRYJYAlakCkoh
CpYgxaLkIu1NvLBeSAStglpqL6xQAsVe2AuL5u2buH3mzGaYPf9AKWTl8d3nl7MzZ2bnazvea9+9
7+PurFWut5e0Zu+s7VybYfKavP7LK3X/5TlM4Q3/OWbyf1ARD/6mgb2SjwtPhbpnq0iKZ6ahrmCj
wqbxdgamRnHOA69jimN5zvIS8cDcUEeVdYzRAw1FHcJYXgPvG4s6Jlgj7xeEequS3wLeNvGvnrEO
tq+Jt82szT+b86+WHlgS2jHGuHF6YHnog1zaupxqCcy3t4X3rVG9iXhgjW+bsFQ80BaxRDywTrF1
VId6toPaqOI2UlsV20ptV2w7tUuxXVSXYl3UvoIZ9kFFPPBJ6D/HLD3QXbwjyDjI6YHPiz5FXiN7
SQ8cDu/N9/1h3veEOP/Oe6gvQnmuvYYe+NL3qYyNVDxw2seF8XKa+jrKJREPnFdx56l+xfqpS4pd
ogZUeQPU91FcKh64GveBeOCaKu8adUM9e4O6reJuU/cUu0c9VM8+pB6r/B5TI+rZEerPUpyhB/6K
5lsqHniuyntO1VR5Nb5CU86FHqZOsTqqXrF66o2ojlQ8zDwVN4+aX86FHqYpXg9YLeevWRzPc7LF
ZG+V1wN6mKXxvMzH6GFaJua5zGNLD7MqmtNcc+hh1oT1oCb5cf6aNj92mbPMGXqY9jCPasLaqQ1h
jMv8pYfZpOI2UR9GcYl4mB1RnMtvB9me8N583B5qb3mNoIf5NGJc1+hhPvPrrjybioc5op49Qh0L
dfj8jlHHQ3s9O059Fc3zRDzMmVKcpYfpU+3oI/umxJyH+TYqLxUPc0X13xVqMMovFQ8zpPIbon6M
WCoeZljVMUz9VIqz9DAP1Dt6QP0a9gpZ7+lhHhXjysreaOhhfiv1vaGH+T2Mv5rbU+hh/uAaOnlN
Xv+Hy4/7mtv3OW5hnpTODIYe5mm0xqbiYf4OcbLv08NU1ZyuuqKLOEvm6sjhJkd8TjRustgkrO3u
vFGjh60r1uyiPHrY6eH84tb7l/SwM8vrAT3snHgNY9wcsoby+Y8edn5UxxTxsIuitrlcFpG9GcVx
/6CHXRrKk72MHrYl3stYB/ceu7I4X02wlWSrCmaF1ehhV7NrovWKHrattI4betj20Fc8r7E87kf2
g+gcy32BHnZDfKZmHPco2xnl4vqlk2yz6r/N1EfRPpiKh90d7VGpeNi9inGPst2lNdbSwx4McS8k
7iDVE/Ytz3qoXsV6qZOKnaTOBDYqjPuRPRfOkz7uHNUf4uQMQg/7XekMYulhB6JnE/GwP0T1JuJh
ryrGM6G9HuWSiIcdDnPmhTs70sPeCuPes1vUXcXuUvcDGxV2n/olOisn4mEfhfOVby/3KDsSlZeI
h32iGOe0faoY57R9ptgzajTKJREPOx7aJnOfHhUbxov0Mz0qU8v50aMyo/wu6VGZrdhsqqH8fnll
HEEz4zj6DNMxK+4X+gyv8cszyoU+4zfmjNAO9zuXrNGXF1gj2ULFFpI1K9ZMtiww//22jGwFXg39
535XkK0O+cl5gz7Du6iP5wd9hvfDs9LP9BnWR/U6tp6sU7FOsi1RLo5tIdsWled+t5HtVO3YSdal
WBfZftW2/WQHVH4HyA6F9+GfPUR2VOV3lKxXsV6yE4qdIDul2Cmys6ptZ8n6Qi7+m7OP7ELoU/8t
dIHsoo8L+V0ku6xyvkw2qNgg2VBgvg+GyK6XyrP0GW5ydE3EuXd5k+xOeOdVibtD9jNm/Qv15O4i"""

# courbB08.pbm font file uuencoded
courB08_pbm ="""eJxNkntM01cUx8+P2/1apUAZEpECq4KRjKhF0E55FYEp4yG6mglz2Q8Q1BhERhhls/zKI+CID4wb
IAPKpk4GAzqZPKKMX2GIUwGJG+ImtKwKjIzXcGuBtncV0Hn+uLnn5Nzv55xv7mdRkbusVjquBACr
0N3B+wCQi/m+ijAf4LGl/wgAiwkNDpRIyyABSjGkBQ/fa3c1bfLs4U8ulDcYUs/502rTpIlO9pyc
Kp/Buql6f3rmZ1NqvpO2SZXf0duY3j0563zjoZpW8AvHRmVeZ/Co36mFR8bERzlsxOMJ+oJshsS5
7rlfzFzmnZFEFnIEZjTGizgLsLzjl4QtrNprBRu10e+u9GgePHjG63bPDw/H87uix0Vtsvkqg9qO
lUimPLiOM4z69YfqIu5Pa2Sr/io6n9Xmf9e+57W1Iapo4lLQBdLSWc/z3KOSlgznDXTW/Flh21kX
IeUIX8FZVL9dwP4NBH5jglYxkBNFmWgMcfsAxM/9gEL5TTwYpnfElR8qQ+WiCgeTHOAfb2bW/cQC
/FozFOOQzAebtjRvQLI7HBtXvaZe25a3Q/1vZpPa+kd1XXKuflr5Cm48YUsUcjMXjsm/sf+22s6z
QAbGZ8mEXMzSE4y9AHhRpltwB1N9ynz5H2MOi0MEi4E5O1ov9ogrFU5cMWAcdgQb3xHFtFK+0pkh
VnYWxltx92j69p6jJ9OnHr+Cq5x5X6Mz70JcX2tEG5LIShM4EHIGoLIRsHzcvEuGwMYA4DZPn7gP
MA1QIgltnt82cTu7j5n76mmz3TU5Bh3PFRTHku52aBgaTnJD7m1c0a3hNjbWWjBtMsP/OFac/LYA
NAAWepdYodB58NBFIuOjNSQ4cgXplqP2RyOe8fd999T8weqBRwLwNFdQobHgA1/YTV8PH+TwV59v
Bo7Y1J4rmHFv3T9e8rmmXdGSuPpSbBnhYJ7V8ICz6AfGcdTpRkpCUU8WcOT8wb+dSHIb6QZapx0M
Y2DO4i7jYV2AUNkkErpQFHVYmFRmYD7OJhDyQSiow4IkrS3TbpQqFA9slE4jnj6peXMTC+N8buJ2
0Uv5eOothuGIiluyCDtff3miBzJHjncOIC3bPT8FLabRPd0TCWy346Mmn9Rz23WyNMJcsnqhQani
3CMFOZuYU7c20zTNVqNbGPNxALWnybeLEcTvXWpc10leI5ae/CI9qBqI686cnO6P6F33e2vAp0nz
9+hnbNeueh/261UJK5aVeSf73ZSXA7dOBXvkXODEb9hVww4KtPNAbPvaZbi0q9kICCl+CiBJSzLv
a8TlntYlC4UHvCRTlaXOy13VAbN0eae2v3hNesWXLsWPkjfOPq7e6zd1fOfc1TckDaylrvleinnT
8Ui87ScLMVhhEx7SUJ8U2zKrRR2Z1dEqZlkr7kDTuhFjpkvse9ZXN0R9H+DlYA4TXVm6/kXDQMyT
eGnJFXlLlSgva5iLUEcbiyDzNqf4Wr9kKYVUIcY40DrnsW4E4zW9QxnHVYx+bo64mIskDWjZgCrq
eVQFrS7Sh/uFLftIidKWbgj6Oq652d4c3v88Dw2JDK7bSWX/ByuaLZI="""

class Code128:
   CharSetA =  {
                ' ':0, '!':1, '"':2, '#':3, '$':4, '%':5, '&':6, "'":7,
                '(':8, ')':9, '*':10, '+':11, ',':12, '-':13, '.':14, '/':15,
                '0':16, '1':17, '2':18, '3':19, '4':20, '5':21, '6':22, '7':23,
                '8':24, '9':25, ':':26, ';':27, '<':28, '=':29, '>':30, '?':31,
                '@':32, 'A':33, 'B':34, 'C':35, 'D':36, 'E':37, 'F':38, 'G':39,
                'H':40, 'I':41, 'J':42, 'K':43, 'L':44, 'M':45, 'N':46, 'O':47,
                'P':48, 'Q':49, 'R':50, 'S':51, 'T':52, 'U':53, 'V':54, 'W':55,
                'X':56, 'Y':57, 'Z':58, '[':59, '\\':60, ']':61, '^':62, '_':63,
                '\x00':64, '\x01':65, '\x02':66, '\x03':67, '\x04':68, '\x05':69, '\x06':70, '\x07':71,
                '\x08':72, '\x09':73, '\x0A':74, '\x0B':75, '\x0C':76, '\x0D':77, '\x0E':78, '\x0F':79,
                '\x10':80, '\x11':81, '\x12':82, '\x13':83, '\x14':84, '\x15':85, '\x16':86, '\x17':87,
                '\x18':88, '\x19':89, '\x1A':90, '\x1B':91, '\x1C':92, '\x1D':93, '\x1E':94, '\x1F':95,
                'FNC3':96, 'FNC2':97, 'SHIFT':98, 'Code C':99, 'Code B':100, 'FNC4':101, 'FNC1':102, 'START A':103,
                'START B':104, 'START C':105, 'STOP':106
           }

   CharSetB = {
                ' ':0, '!':1, '"':2, '#':3, '$':4, '%':5, '&':6, "'":7,
                '(':8, ')':9, '*':10, '+':11, ',':12, '-':13, '.':14, '/':15,
                '0':16, '1':17, '2':18, '3':19, '4':20, '5':21, '6':22, '7':23,
                '8':24, '9':25, ':':26, ';':27, '<':28, '=':29, '>':30, '?':31,
                '@':32, 'A':33, 'B':34, 'C':35, 'D':36, 'E':37, 'F':38, 'G':39,
                'H':40, 'I':41, 'J':42, 'K':43, 'L':44, 'M':45, 'N':46, 'O':47,
                'P':48, 'Q':49, 'R':50, 'S':51, 'T':52, 'U':53, 'V':54, 'W':55,
                'X':56, 'Y':57, 'Z':58, '[':59, '\\':60, ']':61, '^':62, '_':63,
                '' :64, 'a':65, 'b':66, 'c':67, 'd':68, 'e':69, 'f':70, 'g':71,
                'h':72, 'i':73, 'j':74, 'k':75, 'l':76, 'm':77, 'n':78, 'o':79,
                'p':80, 'q':81, 'r':82, 's':83, 't':84, 'u':85, 'v':86, 'w':87,
                'x':88, 'y':89, 'z':90, '{':91, '|':92, '}':93, '~':94, '\x7F':95,
                'FNC3':96, 'FNC2':97, 'SHIFT':98, 'Code C':99, 'FNC4':100, 'Code A':101, 'FNC1':102, 'START A':103,
                'START B':104, 'START C':105, 'STOP':106
           }

   CharSetC = {
                '00':0, '01':1, '02':2, '03':3, '04':4, '05':5, '06':6, '07':7,
                '08':8, '09':9, '10':10, '11':11, '12':12, '13':13, '14':14, '15':15,
                '16':16, '17':17, '18':18, '19':19, '20':20, '21':21, '22':22, '23':23,
                '24':24, '25':25, '26':26, '27':27, '28':28, '29':29, '30':30, '31':31,
                '32':32, '33':33, '34':34, '35':35, '36':36, '37':37, '38':38, '39':39,
                '40':40, '41':41, '42':42, '43':43, '44':44, '45':45, '46':46, '47':47,
                '48':48, '49':49, '50':50, '51':51, '52':52, '53':53, '54':54, '55':55,
                '56':56, '57':57, '58':58, '59':59, '60':60, '61':61, '62':62, '63':63,
                '64':64, '65':65, '66':66, '67':67, '68':68, '69':69, '70':70, '71':71,
                '72':72, '73':73, '74':74, '75':75, '76':76, '77':77, '78':78, '79':79,
                '80':80, '81':81, '82':82, '83':83, '84':84, '85':85, '86':86, '87':87,
                '88':88, '89':89, '90':90, '91':91, '92':92, '93':93, '94':94, '95':95,
                '96':96, '97':97, '98':98, '99':99, 'Code B':100, 'Code A':101, 'FNC1':102, 'START A':103,
                'START B':104, 'START C':105, 'STOP':106
           }


   ValueEncodings = {  0:'11011001100',  1:'11001101100',  2:'11001100110', 
        3:'10010011000',  4:'10010001100',  5:'10001001100',
        6:'10011001000',  7:'10011000100',  8:'10001100100',
        9:'11001001000', 10:'11001000100', 11:'11000100100',
        12:'10110011100', 13:'10011011100', 14:'10011001110',
        15:'10111001100', 16:'10011101100', 17:'10011100110',
        18:'11001110010', 19:'11001011100', 20:'11001001110',
        21:'11011100100', 22:'11001110100', 23:'11101101110',
        24:'11101001100', 25:'11100101100', 26:'11100100110',
        27:'11101100100', 28:'11100110100', 29:'11100110010',
        30:'11011011000', 31:'11011000110', 32:'11000110110',
        33:'10100011000', 34:'10001011000', 35:'10001000110',
        36:'10110001000', 37:'10001101000', 38:'10001100010',
        39:'11010001000', 40:'11000101000', 41:'11000100010',
        42:'10110111000', 43:'10110001110', 44:'10001101110',
        45:'10111011000', 46:'10111000110', 47:'10001110110',
        48:'11101110110', 49:'11010001110', 50:'11000101110',
        51:'11011101000', 52:'11011100010', 53:'11011101110',
        54:'11101011000', 55:'11101000110', 56:'11100010110',
        57:'11101101000', 58:'11101100010', 59:'11100011010',
        60:'11101111010', 61:'11001000010', 62:'11110001010',
        63:'10100110000', 64:'10100001100', 65:'10010110000',
        66:'10010000110', 67:'10000101100', 68:'10000100110',
        69:'10110010000', 70:'10110000100', 71:'10011010000',
        72:'10011000010', 73:'10000110100', 74:'10000110010',
        75:'11000010010', 76:'11001010000', 77:'11110111010',
        78:'11000010100', 79:'10001111010', 80:'10100111100',
        81:'10010111100', 82:'10010011110', 83:'10111100100',
        84:'10011110100', 85:'10011110010', 86:'11110100100',
        87:'11110010100', 88:'11110010010', 89:'11011011110',
        90:'11011110110', 91:'11110110110', 92:'10101111000',
        93:'10100011110', 94:'10001011110', 95:'10111101000',
        96:'10111100010', 97:'11110101000', 98:'11110100010',
        99:'10111011110',100:'10111101110',101:'11101011110',
        102:'11110101110',103:'11010000100',104:'11010010000',
        105:'11010011100',106:'11000111010'
                        }

   def makeCode(self, code):
      """ Create the binary code
      return a string which contains "0" for white bar, "1" for black bar """
      
      current_charset = None
      pos=sum=0
      skip=False
      strCode=""
      for c in range(len(code)):
          if skip:
              skip=False
              continue
        
          #Only switch to char set C if next four chars are digits
          if len(code[c:]) >=4 and code[c:c+4].isdigit() and current_charset!=self.CharSetC or \
             len(code[c:]) >=2 and code[c:c+2].isdigit() and current_charset==self.CharSetC:     
             #If char set C = current and next two chars ar digits, keep C 
             if current_charset!=self.CharSetC:
                 #Switching to Character set C
                 if pos:
                     strCode += self.ValueEncodings[current_charset['Code C']]
                     sum  += pos * current_charset['Code C']
                 else:
                     strCode= self.ValueEncodings[self.CharSetC['START C']]
                     sum = self.CharSetC['START C']
                 current_charset= self.CharSetC
                 pos+=1
          elif self.CharSetB.has_key(code[c]) and current_charset!=self.CharSetB and \
               not(self.CharSetA.has_key(code[c]) and current_charset==self.CharSetA): 
             #If char in chrset A = current, then just keep that
             # Switching to Character set B
             if pos:
                 strCode += self.ValueEncodings[current_charset['Code B']]
                 sum  += pos * current_charset['Code B']
             else:
                 strCode= self.ValueEncodings[self.CharSetB['START B']]
                 sum = self.CharSetB['START B']
             current_charset= self.CharSetB
             pos+=1
          elif self.CharSetA.has_key(code[c]) and current_charset!=self.CharSetA and \
               not(self.CharSetB.has_key(code[c]) and current_charset==self.CharSetB): 
             # if char in chrset B== current, then just keep that
             # Switching to Character set A
             if pos:
                 strCode += self.ValueEncodings[current_charset['Code A']]
                 sum  += pos * current_charset['Code A']
             else:
                 strCode += self.ValueEncodings[self.CharSetA['START A']]
                 sum = self.CharSetA['START A']
             current_charset= self.CharSetA
             pos+=1

          if current_charset==self.CharSetC:
             val= self.CharSetC[code[c:c+2]]
             skip=True
          else:
             val=current_charset[code[c]]

          sum += pos * val
          strCode += self.ValueEncodings[val]
          pos+=1
                        
      #Checksum
      checksum= sum % 103
            
      strCode +=  self.ValueEncodings[checksum]
                    
      #The stop character
      strCode += self.ValueEncodings[current_charset['STOP']]
                    
      #Termination bar
      strCode += "11"
            
      return strCode

   def getImage(self, value, height = 50, extension = "PNG"):
      """ Get an image with PIL library 
      value code barre value
      height height in pixel of the bar code
      extension image file extension"""
      import Image, ImageFont, ImageDraw
      from string import lower, upper
      
      # Create a missing font file
      decodeFontFile(courB08_pil ,"courB08.pil")
      decodeFontFile(courB08_pbm ,"courB08.pbm")
      
      # Get the bar code list
      bits = self.makeCode(value)
      
      # Create a new image
      position = 8
      im = Image.new("1",(len(bits)+position,height))
      
      # Load font
      font = ImageFont.load("courB08.pil")
      
      # Create drawer
      draw = ImageDraw.Draw(im)
      
      # Erase image
      draw.rectangle(((0,0),(im.size[0],im.size[1])),fill=256)
      
      # Draw text
      draw.text((0, height-9), value, font=font, fill=0)
      
      # Draw the bar codes
      for bit in range(len(bits)):
         if bits[bit] == '1':
            draw.rectangle(((bit+position,0),(bit+position,height-10)),fill=0)
            
      # Save the result image
      im.save(value+"."+lower(extension), upper(extension))


def decodeFontFile(data, file):
   """ Decode font file embedded in this script and create file """
   from zlib import decompress
   from base64 import decodestring
   from os.path import exists
   
   # If the font file is missing
   if not exists(file):
      # Write font file
      open (file, "wb").write(decompress(decodestring(data)))

def testWithChecksum():
   """ Test bar code with checksum """
   bar = Code128()
   assert(bar.makeCode('HI345678')=='11010010000110001010001100010001010111011110100010110001110001011011000010100100001001101100011101011')

def testImage():
   """ Test images generation with PIL """
   bar = Code128()
   bar.getImage("9782212110708",50,"gif")
   bar.getImage("978221211070",50,"png")

def test():
   """ Execute all tests """
   testWithChecksum()
   testImage()

if __name__ == "__main__":
   test()

