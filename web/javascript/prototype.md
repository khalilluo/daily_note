https://blog.csdn.net/qq_34645412/article/details/105997336


当我们调用一个对象的属性时，如果对象没有该属性，JavaScript 解释器就会从对象的原型对象上去找该属性，如果原型上也没有该属性，那就去找原型的原型，直到最后返回null为止，null没有原型。这种属性查找的方式被称为原型链（prototype chain）


``` js
Array.prototype.__proto_.toString === Object.prototype.toString // true，原型链

var TestPrototype = function () {
    this.propA = 1;
    this.methodA = function() {
        return this.propA;
    }
}

TestPrototype.prototype = {
    methodB: function() {
        return this.propA;
    }
}

var objA = new TestPrototype();

objA.methodA() // 1
objA.methodB() // 1


var objB = new TestPrototype();

objA.methodA === objA.methodA // false
objA.methodB === objA.methodB // true
```

把方法写在prototype属性上就有效的减少了这种成本（他们指向了同一个methodB）。多个对象之间共享原型proto


### 圣杯模式

``` js
function Father(){}
function Son(){}
Father.prototype.lastName=‘Jack‘;

//圣杯模式
function inherit(Target,Origin){
	function F(){};
	F.prototype=Origin.prototype;
	Target.prototype=new F();
}

inherit(Son,Father);
var son=new Son();
var father=new Father();

Son.prototype.sex=‘male‘;
// 沿着__proto__(即原型链）往上找， 即在函数F中找是否存在该属性。F和Father的prototype都是指向Father.prototype
console.log(son.lastName);//Jack
console.log(son.sex);//male

// 最后，由于有中间层F的存在，因此Father的prototype自始至终都没有受到影响
console.log(father.sex);//undefined
```