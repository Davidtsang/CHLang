using MyHandle = int32_t *;

int32_t GetGlobalValue();
int32_t n = 8;

class IMyInterface {
public:
  virtual ~IMyInterface() {} // Virtual destructor
  virtual void onEvent() = 0;
};

struct MyPoint {
public:
  int32_t x;
  int32_t y;

private:
  MyPoint(int32_t x, int32_t y);
  virtual int32_t getSum();
};

class MyClass : public IMyInterface {
private:
  std::string m_name = "default";
  MyHandle m_handle;
  MyClass(int32_t id);
  MyClass();
  virtual MyClass *create();
  virtual std::string getName();
  virtual void setName(std::string name);
  virtual void onEvent();

public:
  int32_t m_id;
  virtual ~MyClass();
};
